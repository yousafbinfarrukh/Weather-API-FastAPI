from fastapi import FastAPI
from .routers import weather

app = FastAPI()
app.include_router(weather.router)

