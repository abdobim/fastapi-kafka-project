from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.kafka_producer import send_message_to_kafka
from app.dependencies import role_required

router = APIRouter()


class Message(BaseModel):
    content: str


@router.post("/submit", dependencies=[Depends(role_required("admin"))])
def submit_message(message: Message):
    send_message_to_kafka(message.dict())
    return {"status": "submitted"}
