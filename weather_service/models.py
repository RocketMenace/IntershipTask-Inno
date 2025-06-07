from django.db import models


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
        ordering = ["created_at"]
        indexes = [models.Index(fields=["city"])]
        verbose_name = "forecast_record"
        verbose_name_plural = "forecast_records"
