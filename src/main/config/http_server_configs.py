from fastapi import FastAPI
from src.main.routes import startships_routes

app = FastAPI()

app.include_router(startships_routes)
