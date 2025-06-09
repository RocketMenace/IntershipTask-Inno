from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    OpenApiParameter,
)
from rest_framework import status
from .serializers import (
    CurrentWeatherSerializer,
    TemperatureForecastSerializer,
    CreateForecastSerializer,
)
from datetime import date


temperature_forecast = extend_schema(
    methods=["GET", "POST"],
    tags=["Weather"],
    summary="Get weather forecast.",
    description="Retrieve min/max temperature forecast for a specific city and date",
    responses={
        200: TemperatureForecastSerializer,
        400: OpenApiResponse(
            response=CreateForecastSerializer,
            description="Validation Error",
            examples=[
                OpenApiExample(
                    "Invalid city",
                    value={
                        "error": "Validation Error",
                        "details": {
                            "city": "Country names can only contain English letters."
                        },
                    },
                    status_codes=["400"],
                ),
                OpenApiExample(
                    "Invalid date",
                    value={
                        "error": "Validation Error",
                        "details": {"date": "Date cannot be in the past"},
                    },
                    status_codes=["400"],
                ),
            ],
        ),
    },
    parameters=[
        OpenApiParameter(
            name="city",
            description="City name (English letters only)",
            required=True,
            type=str,
            examples=[
                OpenApiExample("London", value="London"),
                OpenApiExample("New York", value="New York"),
            ],
        ),
        OpenApiParameter(
            name="date",
            description="Date in DD.MM.YYYY format",
            required=True,
            type=date,
            examples=[
                OpenApiExample("Today", value="15.06.2023"),
                OpenApiExample("Future date", value="20.06.2023"),
            ],
        ),
    ],
)


current_weather_docs = extend_schema(
    tags=["Weather"],
    methods=["GET"],
    summary="Get current temperature",
    description="Returns current temperature and local time for specified city",
    parameters=[
        OpenApiParameter(
            name="city", description="Getting current weather", required=True, type=str
        )
    ],
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            description="",
            response=CurrentWeatherSerializer,
            examples=[
                OpenApiExample(
                    name="Successful response",
                    response_only=True,
                    value={"temperature": 22.1, "local_time": "16:45"},
                )
            ],
        )
    },
)
