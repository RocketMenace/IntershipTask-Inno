from django.urls import path
from .apps import WeatherServiceConfig

from .views import CurrentWeatherAPIView

app_name = WeatherServiceConfig.name

urlpatterns = [
    path("current", CurrentWeatherAPIView.as_view(), name="current_weather"),
]
