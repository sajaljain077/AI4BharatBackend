from fastapi import FastAPI, APIRouter
from controller import endpoints


api_router = APIRouter()
api_router.include_router(endpoints.router, tags=["end_points"])