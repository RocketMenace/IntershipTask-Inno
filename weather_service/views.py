from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    CurrentWeatherSerializer,
    TemperatureForecastSerializer,
    CreateForecastSerializer,
)
from .services import get_weather_data, get_weather_data_on_date, create_forecast_record
from .views_docs import current_weather_docs, temperature_forecast


@current_weather_docs
class CurrentWeatherAPIView(APIView):
    serializer_class = CurrentWeatherSerializer

    def get(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            weather_data = get_weather_data(request.query_params)
            return Response(
                data=serializer.to_internal_value(weather_data),
                status=status.HTTP_200_OK,
            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@temperature_forecast
class TemperatureForecastAPIView(APIView):
    serializer_class = TemperatureForecastSerializer

    def get(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            weather_data = get_weather_data_on_date(request.query_params)
            output_serializer = self.serializer_class(weather_data)
            return Response(
                data=output_serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: Request) -> Response:
        serializer = CreateForecastSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            record = create_forecast_record(serializer.validated_data)
            output_serializer = CreateForecastSerializer(record)
            return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
