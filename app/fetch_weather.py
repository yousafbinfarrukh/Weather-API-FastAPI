from fastapi import HTTPException
import httpx
import os
from dotenv import load_dotenv
from functools import lru_cache

@lru_cache(maxsize=100)
def get_weather_data(endpoint: str, params: dict) -> dict:
    response = httpx.get(endpoint, params=params)
    print('Made a call')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data")
    return response.json()

async def fetch_weather_data(endpoint: str, params: dict) -> dict:
    return get_weather_data(endpoint, tuple(sorted(params.items())))

