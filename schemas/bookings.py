from typing import Optional
from enum import Enum
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field


class Bookings(BaseModel):
    booking_id: Optional[int] = Field(gt=0)
    user_id: int = Field(...,gt=0)
    destiny: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="Miami"
        )
    payment_method: str = Field(
        ...,
        min_length=0,
        max_length=20,
        example="Cash"
        )
    amount_of_booking: int = Field (...,gt=20, example=300)
    created_at: datetime = Field(default=datetime.now())
    status: int = Field(default=1)
    
    class Config:
        orm_mode =True