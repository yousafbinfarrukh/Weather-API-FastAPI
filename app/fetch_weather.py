from fastapi import HTTPException
import httpx
import time
from collections import OrderedDict

class TimeBasedCache:
    def __init__(self, expiration_seconds=3600, max_entries=100):
        self.cache = OrderedDict()
        self.expiration_seconds = expiration_seconds
        self.max_entries = max_entries

    def get(self, key):
        current_time = time.time()
        if key in self.cache:
            value, timestamp = self.cache[key]
            if current_time - timestamp < self.expiration_seconds:
                self.cache.move_to_end(key)
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key, value):
        if len(self.cache) >= self.max_entries:
            self.cache.popitem(last=False)
        self.cache[key] = (value, time.time())

cache = TimeBasedCache(expiration_seconds=3600, max_entries=100)  

async def fetch_weather_data_from_api(endpoint: str, params: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail='Failed to fetch weather data')
        return response.json()

async def fetch_weather_data(endpoint: str, params: dict) -> dict:
    cache_key = f'{endpoint}:{tuple(sorted(params.items()))}'
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    print('making a call')
    data = await fetch_weather_data_from_api(endpoint, params)
    cache.set(cache_key, data)
    return data
