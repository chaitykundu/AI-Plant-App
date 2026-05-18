from fastapi import FastAPI
from app.api.routes.plant_routes import router

app = FastAPI(
    title="Plant AI Backend"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Plant AI API Running"}