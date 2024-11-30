from django.urls import path
from .views import TestCreateAPIView, PatientTestsAPIView, StatsAPIView, BatchUploadAPIView

urlpatterns = [
    path('api/tests/', TestCreateAPIView.as_view(), name='create-test'),
    path('api/tests/', PatientTestsAPIView.as_view(), name='patient-tests'),
    path('api/tests/stats/', StatsAPIView.as_view(), name='test-stats'),
    path('api/tests/batch-upload/',
         BatchUploadAPIView.as_view(), name='batch-upload')
]
