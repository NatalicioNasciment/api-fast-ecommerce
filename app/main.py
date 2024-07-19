from fastapi import FastAPI
from app.routers.category_routes import router as category_routers

app = FastAPI()

@app.get('/health-check')
def health_check():
    return True

app.include_router(category_routers)