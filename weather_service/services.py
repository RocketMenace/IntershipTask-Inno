import os
from typing import Any
from datetime import datetime

from rest_framework.exceptions import APIException

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
