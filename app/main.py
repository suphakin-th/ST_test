from fastapi import FastAPI
from app.route.items import router as items_router

app = FastAPI()

app.include_router(items_router, prefix="/items", tags=["items"])
