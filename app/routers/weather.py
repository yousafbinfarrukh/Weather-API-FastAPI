from fastapi.routing import APIRouter
from typing import Optional
import os
from .. import schemas
from .. import fetch_weather
from dotenv import load_dotenv

router = APIRouter(
    prefix='/weather',
    tags=['weather']
)

env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env')
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv('WEATHER_API_KEY')
if not API_KEY:
    raise ValueError('No API key found. Please set the WEATHER_API_KEY environment variable.')

BASE_URL = 'http://api.weatherapi.com/v1'

@router.get('/weather/current', response_model=schemas.WeatherResponse)
async def get_current_weather(location: str):
    endpoint = f'{BASE_URL}/current.json'
    params = {'key': API_KEY, 'q': location}
    data = await fetch_weather.fetch_weather_data(endpoint, params)
    return data

@router.get('/weather/forecast', response_model=schemas.ForecastResponse)
async def get_weather_forecast(location: str, days: Optional[int] = 3):
    endpoint = f'{BASE_URL}/forecast.json'
    params = {'key': API_KEY, 'q': location, 'days': days}
    data = await fetch_weather.fetch_weather_data(endpoint, params)
    return data