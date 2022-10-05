from typing import List
from typing import Union
from fastapi import status
from fastapi import Path, Query
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from connections import SessionLocal,engine
from sqlalchemy.orm import Session
from fastapi.params import Depends

import models
from schemas.bookings import Bookings

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get(path="/bookings/{booking_id}",
            response_model=Bookings,
            status_code=status.HTTP_200_OK, 
            summary="Show a valid booking",
            tags=["Bookings"])
def show_booking(booking_id:int = Path(...,gt=0),db:Session=Depends(get_db)):
    """
    ## This path operation shows a valid booking in the app.

    **- Parameters:** 
    - booking_id: int

    **Returns a json with a valid booking in the app, with the following keys:**
    - booking_id: int Primary Key
    - user_id: int FK
    - destiny: str
    - payment_method: str
    - amount_of_booking: float
    - created_at: datetime Field
    - status: int
               
    """
    try:
        booking = db.query(models.Bookings).filter_by(booking_id=booking_id).first()
        db.commit()
        db.refresh(booking)
        return booking
    except Exception as error:
        print(error)
        return JSONResponse(status_code=404, content={'message':'booking Not Found.'})
    
    
@router.get(
    path="/bookings",
    response_model=List[Bookings],
    status_code=status.HTTP_200_OK,
    summary="Show All Bookings",
    tags=["Bookings"])
def show_bookings(db:Session=Depends(get_db), 
                  user_id: int = Query(default=1), 
                  amount_of_booking: int = Query(default=0),
                  destiny: str = Query(default="Miami"),
                  skip: int = Query(default=0) , limit: Union[int, None] = None):
    """
    ## This path operation shows all bookings in the app.

    **- Parameters:** 
    -

    **Returns a json list with all bookings in the app, with the following keys:**
    - booking_id: int Primary Key
    - user_id: int FK
    - destiny: str
    - payment_method: str
    - amount_of_booking: float
    - created_at: datetime Field
    - status: int
                
    """
    bookings= db.query(models.Bookings).all()
    return bookings

@router.post(
    path="/bookings",
    response_model=Bookings,
    status_code=status.HTTP_201_CREATED,
    summary="Post a booking",
    tags=["Bookings"])
def post_booking(entry_point:Bookings,db:Session=Depends(get_db)):
    """
    ## This path operation post a booking in the app.

    **- Parameters:**
    - booking: Bookings

    **Returns a json body with a message:** 
    - message: "Booking Saved successfully"

    """
    try:
        booking = models.Bookings(user_id = entry_point.user_id,
                                  destiny = entry_point.destiny,
                                  payment_method = entry_point.payment_method,
                                  amount_of_booking = entry_point.amount_of_booking,
                                  created_at = entry_point.created_at,
                                  status = entry_point.status)
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return JSONResponse(status_code=201, content={'message': "Booking Saved successfully"})
    except:
        return JSONResponse(status_code=500, content={'message': "Sorry, there is an error"})


@router.delete(
    path="/bookings/{booking_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a Booking",
    tags=["Bookings"])
def delete_booking(booking_id:int= Path(...,gt=0),db:Session=Depends(get_db)):
    """
    ## This path operation delete a booking in the app.

    **- Parameters:**
    - booking_id: int

    **Returns a json body with a message:** 
    - message: "Booking Deleted"

    """
    try:
        booking = db.query(models.Bookings).filter_by(booking_id=booking_id).first()
        db.delete(booking)
        db.commit()
        return JSONResponse(status_code=200, content={'message': "Your Booking was deleted"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=404, content={'message':'booking Not Found.'})