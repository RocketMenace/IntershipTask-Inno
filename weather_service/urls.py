from django.urls import path
from .apps import WeatherServiceConfig

from .views import CurrentWeatherAPIView, TemperatureForecastAPIView

app_name = WeatherServiceConfig.name

urlpatterns = [
    path("current", CurrentWeatherAPIView.as_view(), name="current_weather"),
    path("forecast", TemperatureForecastAPIView.as_view(), name="temp_forecast"),
]
