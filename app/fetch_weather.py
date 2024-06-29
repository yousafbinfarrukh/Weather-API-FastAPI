from fastapi import HTTPException
import httpx
import os
from dotenv import load_dotenv

async def fetch_weather_data(endpoint: str, params: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data")
        return response.json()
