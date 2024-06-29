from pydantic import BaseModel

class WeatherResponse(BaseModel):
    location: dict
    current: dict


class ForecastResponse(BaseModel):
    location: dict
    forecast: dict