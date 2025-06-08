from rest_framework import serializers


class CurrentWeatherSerializer(serializers.Serializer):

    city = serializers.CharField(required=True, write_only=True)
    temperature = serializers.FloatField(read_only=True)
    local_time = serializers.TimeField(format="HH:mm", read_only=True)


# class TemperatureForecastSerializer(serializers.Serializer):


