import re

from rest_framework import serializers
from datetime import datetime

from rest_framework.exceptions import ValidationError


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
    pass
