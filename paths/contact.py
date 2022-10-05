from pydantic import EmailStr
from fastapi import status
from fastapi import Form
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.contact import Contact


router = APIRouter()


@router.post(
    path="/contact", 
    status_code=status.HTTP_201_CREATED, 
    summary="Contact Form",
    tags=["Contact Us"])
def contact(
    name: str=Form(
        ...,
        min_length=5,
        max_length=20),
    email: EmailStr = Form(...), 
    comments: str =Form(
        ...,
        min_length=5,
        max_length=250)):
    """
    ## This path operation is for direct contact with fivestarscarservice.com

    **- Request body parameter:**
    - **Form**:
        mane: str
        email: EmailStr
        comments: str

    **Returns a confirmation message:**
    - "Thank you very much for sending your message, we will contact you shortly."
        
    """
    return JSONResponse(status_code=201, content={'message': "Thank you very much for sending your message, we will contact you shortly."})