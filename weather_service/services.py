import os
from typing import Any

from rest_framework.exceptions import APIException
from .models import ForecastRecord
from  datetime import datetime

WEATHER_SERVICE_API_KEY = os.getenv("WEATHER_SERVICE_API_KEY")

import httpx


def get_weather_data(data: dict[str, Any]) -> dict[str, Any]:
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"q": data.get("city"), "key": WEATHER_SERVICE_API_KEY}
    response = httpx.get(url=url, params=params)
    if response.status_code == 200:
        local_time = response.json().get("location").get("localtime")
        temperature = response.json().get("current").get("temp_c")
        return {"temperature": temperature, "local_time": local_time}
    raise APIException(detail=response.json())


def get_weather_data_on_date(data: dict[str, Any]) -> dict[str, Any]:
    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "q": data.get("city"),
        "dt": data.get("date"),
        "key": WEATHER_SERVICE_API_KEY,
    }
    response = httpx.get(url=url, params=params)
    if response.status_code == 200:
        min_temperature = (
            response.json()
            .get("forecast")
            .get("forecastday")[0]
            .get("day")
            .get("mintemp_c")
        )
        max_temperature = (
            response.json()
            .get("forecast")
            .get("forecastday")[0]
            .get("day")
            .get("maxtemp_c")
        )
        format_date = datetime.strptime(response.json().get("location").get("localtime"), "%Y-%m-%d %H:%M").date()
        forecast_record = ForecastRecord.objects.create(
            city=data.get("city"),
            date=format_date,
            min_temperature=min_temperature,
            max_temperature=max_temperature,
        )
        return forecast_record
    raise APIException(detail=response.json())
