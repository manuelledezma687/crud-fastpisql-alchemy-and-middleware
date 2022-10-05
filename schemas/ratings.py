from typing import Optional
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field


class Ratings(BaseModel):
    rating_id: Optional[int] = Field(gt=0)
    user_id: int = Field(...,gt=0)
    travel_id: int =Field(...,gt=0)
    stars: int = Field(..., gt=0, le=5)
    comments: str = Field(
        ...,
        min_length=0,
        max_length=140,
        example="Hi it is a excelent service."
        )
    created_at: datetime = Field(default=datetime.now())
    status: int = Field(default=1)
    
    class Config:
        orm_mode =True