from typing import List, Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, model_validator

class HistoryItem(BaseModel):
    timestamp: datetime
    sender: str
    message: str

class RequestModel(BaseModel):
    conversation_id: UUID
    user_id: UUID
    conversation_history: List[HistoryItem]
    last_message: Optional[str]
    query: str
    task_prompt: Optional[str]
    timestamp: datetime

    @model_validator(mode="before")
    def check_nullable_keys(cls, data):
        missing = [k for k in ("last_message", "task_prompt") if k not in data]
        if missing:
            raise ValueError(f"Key(s) {missing} required by the contract.")
        return data

    class Config:
        extra = "allow"
