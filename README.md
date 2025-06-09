# Weather Forecast API 🌦️

[![Django](https://img.shields.io/badge/Django-3.2-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)


## 📝 Description
A RESTful API for managing and retrieving temperature forecasts with:
- City-based weather data
- Date-specific forecasts
- Min/max temperature recording
- Data validation and constraints

## ✨ Features
- **Temperature Forecasts**: Get min/max temperatures for cities
- **Data Validation**: 
  - English-only city names
  - Future date constraints (max +10 days)
  - Temperature integrity checks
- **Swagger Documentation**: Interactive API documentation
- **Dockerized**: Easy setup with PostgreSQL

## 🔌 API Endpoints

| Endpoint                 | Method | Description             | Parameters |
|--------------------------|--------|-------------------------|------------|
| `/api/weather/forecast/` | GET    | Get forecast            | `city`, `date` |
| `/api/weather/forecast/` | POST   | Create forecast         | JSON payload |`
| `/api/weather/current/`  | GET    | Get current temperature | `city` |`


## ⚙️ Configuration
Environment variables (`.env` file):

| Variable | Description | Default |
|----------|-------------|---------|
| `POSTGRES_DB` | Database name | `intership_task` |
| `POSTGRES_USER` | Database user | `postgres` |
| `POSTGRES_PASSWORD` | Database password | - |
| `DJANGO_SECRET_KEY` | Django secret key | - |
| `WEATHER_SERVICE_API_KEY` | Weather API key | - |

## 🛠️ Installation

### Prerequisites
- Docker
- Docker Compose

### Setup
 Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-forecast-api.git
   cd weather-forecast-api
   docker-compose up -d --build
