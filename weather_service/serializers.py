from rest_framework import serializers
from datetime import datetime


class CurrentWeatherSerializer(serializers.Serializer):
    temperature = serializers.FloatField(read_only=True)
    local_time = serializers.TimeField(read_only=True)

    def to_internal_value(self, data):
        data["local_time"] = datetime.strptime(
            data["local_time"], "%Y-%m-%d %H:%M"
        ).time()
        return data


# class TemperatureForecastSerializer(serializers.Serializer):
