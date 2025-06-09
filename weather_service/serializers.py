import re

from rest_framework import serializers
from datetime import datetime, timedelta

from rest_framework.exceptions import ValidationError
from .models import ForecastRecord


class CurrentWeatherSerializer(serializers.Serializer):
    city = serializers.CharField(required=True, write_only=True)
    temperature = serializers.FloatField(read_only=True)
    local_time = serializers.TimeField(read_only=True)

    def validate(self, data):
        city = data.get("city")
        pattern = r"^[a-zA-Z]+$"
        if not re.match(pattern, city):
            raise ValidationError(
                {city: "Country names can only contain English letters."},
            )
        return data

    def to_internal_value(self, data):
        time = data.get("local_time")
        if time:
            data["local_time"] = datetime.strptime(
                data["local_time"], "%Y-%m-%d %H:%M"
            ).time()
        return data


class TemperatureForecastSerializer(serializers.Serializer):
    city = serializers.CharField(required=True, write_only=True)
    date = serializers.DateField(required=True, write_only=True, format="%d.%m.%Y")
    min_temperature = serializers.FloatField(read_only=True)
    max_temperature = serializers.FloatField(read_only=True)

    def validate(self, data):
        city = data.get("city")
        pattern = r"^[a-zA-Z]+$"
        if not re.match(pattern, city):
            raise ValidationError(
                {city: "Country names can only contain English letters."},
            )
        date = data.get("date")
        if date > datetime.today().date() + timedelta(days=10):
            raise ValidationError(
                {"date": "Date can't be bigger than current date more than 10 days."},
            )
        if date < datetime.today().date():
            raise ValidationError(
                {"date": "Past date is not allowed."},
            )
        return data


class CreateForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastRecord
        exclude = ["id", "created_at", "updated_at"]
