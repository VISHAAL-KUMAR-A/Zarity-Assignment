from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.


class Sample(models.Model):
    patient_id = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(10000000)])
    test_name = models.CharField(null=True, max_length=25)
    value = models.DecimalField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1000.00)], decimal_places=2, max_digits=10, null=True)
    unit = models.CharField(null=True, max_length=10)
    test_date = models.DateTimeField(default=timezone.now, null=True)
    is_abnormal = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.patient_id}{self.test_name}"
