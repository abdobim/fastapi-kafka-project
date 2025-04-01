from fastapi import FastAPI
from app.routes import message

app = FastAPI()

app.include_router(message.router, prefix="/messages", tags=["Messages"])
