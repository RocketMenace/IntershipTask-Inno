from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CurrentWeatherSerializer, TemperatureForecastSerializer
from .services import get_weather_data, get_weather_data_on_date


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
