import os
from typing import Any

WEATHER_SERVICE_API_KEY = os.getenv("WEATHER_SERVICE_API_KEY")

import httpx


def get_weather_data(city: str) -> dict[str, Any]:
    url = f"http://api.openweathermap.org/geo/1.0/direct"
    params = {"city": city, "appid": WEATHER_SERVICE_API_KEY}
    response = httpx.get(url=url, params=params)
    print(response.json())
    # response = httpx.get(url=)
    return response.json()

