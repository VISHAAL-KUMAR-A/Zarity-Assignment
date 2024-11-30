from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max
from .models import Sample
from .serializers import SampleSerializer
import pandas as pd
from rest_framework.parsers import MultiPartParser


class TestCreateAPIView(APIView):
    def post(self, request):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientTestsAPIView(APIView):
    def get(self, request):
        patient_id = request.GET.get('patient_id')
        if not patient_id:
            return Response({"error": "Patient ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        tests = Sample.objects.filter(patient_id=patient_id)
        serializer = SampleSerializer(tests, many=True)
        return Response(serializer.data)


class StatsAPIView(APIView):
    def get(self, request):
        stats = Sample.objects.values('test_name').annotate(
            min_value=Min('value'),
            max_value=Max('value'),
            avg_value=Avg('value')
        )
        return Response(stats)


class BatchUploadAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = pd.read_csv(file)
            samples = [
                Sample(
                    patient_id=row['patient_id'],
                    test_name=row['test_name'],
                    value=row['value'],
                    unit=row['unit'],
                    test_date=row['test_date'],
                    is_abnormal=row['is_abnormal'],
                )
                for _, row in data.iterrows()
            ]
            Sample.objects.bulk_create(samples)
            return Response({"message": "Batch upload successful"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
