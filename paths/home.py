from fastapi import status
from fastapi import APIRouter


router = APIRouter()


@router.get(path="/", 
         status_code=status.HTTP_200_OK , 
         summary="Home",
         tags=["Main"])
def home():
    """
    ## Web EndPoints:
        -Users: 
            Login.
            Register an user.
            Update an User.
            Delete an User.
            Show an User.
            Show all Users.
        -Travels: 
            Show travel. 
            Show all travels.
            Post a travel.
        Bookings:
            Show a booking. 
            Show all bookings.
            Post a Booking.
            Delete a Booking.
        -Contact: 
            Post a Form.
        -ratings: 
            Show all ratings
            Show a rating per id
            Post a rating
            
    """
    return "Welcome to this Proyect"