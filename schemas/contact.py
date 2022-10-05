from pydantic import BaseModel, Field, EmailStr
from fastapi import Form


class Contact(BaseModel):
    first_name: str = Field(
        ...,
        max_length=20,
        example="John Smith"
        )
    email: EmailStr = Field(
        ...,
        example="testing@gmail.com"
        )
    comments: str = Field(
        ...,
        max_length=100,
        example="Hi i want to make a reservation."
        )
    