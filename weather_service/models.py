from django.db import models
from datetime import date, timedelta


class BaseModel(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class ForecastRecord(BaseModel):
    city = models.CharField(max_length=255, verbose_name="city")
    date = models.DateField(verbose_name="date")
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()

    class Meta:
        db_table_comment = "ForecastRecords"
        db_table = "forecast_records"
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["city"])]
        verbose_name = "forecast_record"
        verbose_name_plural = "forecast_records"
        constraints = [
            models.CheckConstraint(
                name="max_temp_gte_min_temp",
                check=models.Q(max_temperature__gte=models.F("min_temperature")),
                violation_error_message="Maximum temperature must be greater than or equal to minimum temperature",
            ),
            models.CheckConstraint(
                name="date_between_current_date_and_ten_days_after",
                check=models.Q(date__gte=date.today())
                & models.Q(date__lte=date.today() + timedelta(days=10)),
                violation_error_message="Date can't be lower than current date.",
            ),
        ]
