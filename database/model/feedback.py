from pydantic import BaseModel, Field
from typing import Optional


class UserFeedback(BaseModel):
    text: str
    productId: int


class FeedbackModel(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    productId: int
    userId: str
    text: str
    feedback: str
