from typing import Optional
from datetime import date
from datetime import datetime
from pydantic import BaseModel, Field

class Travels(BaseModel):
    travel_id: Optional[int]= Field(gt=0)
    booking_id: int= Field(...,gt=0)
    created_at: datetime = Field(default=datetime.now())
    status: int = Field(default=1)
    
    class Config:
        orm_mode =True
    
