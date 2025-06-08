from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CurrentWeatherSerializer
from .services import get_weather_data


class CurrentWeatherAPIView(APIView):
    serializer_class = CurrentWeatherSerializer

    def get(self, request: Request):
        weather_data = get_weather_data(request.query_params)
        serializer = self.serializer_class(data=weather_data)
        if serializer.is_valid(raise_exception=True):
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
