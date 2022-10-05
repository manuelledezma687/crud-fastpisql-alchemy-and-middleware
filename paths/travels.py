from typing import List
from fastapi import status
from fastapi import Path, Query
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from connections import SessionLocal,engine
from sqlalchemy.orm import Session
from fastapi.params import Depends
import models
from schemas.travels import Travels

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get(path="/travels/{travel_id}",
            response_model=Travels,
            status_code=status.HTTP_200_OK, 
            summary="Show a valid travel",
            tags=["Travels"])
def show_travel(travel_id:int = Path(...,gt=0),db:Session=Depends(get_db)):
    """
    ## This path operation shows a valid travel in the app.

    **- Parameters:** 
    - travel_id: int

    **Returns a json with a valid travel in the app, with the following keys:**
    - travel_id: int Primary Key
    - booking_id: int FK
    - Created_at: datetime Field
    - status: bool
               
    """
    try:
        travel = db.query(models.Travels).filter_by(travel_id=travel_id).first()
        db.commit()
        db.refresh(travel)
        return travel
    except Exception as error:
        print(error)
        return JSONResponse(status_code=404, content={'message':'travel Not Found.'})


@router.get(
    path="/travels",
    response_model=List[Travels],
    status_code=status.HTTP_200_OK,
    summary="Show All travels",
    tags=["Travels"])
def show_travels(db:Session=Depends(get_db),skip: int = Query(default=0) , limit: int = Query(default=10)):
    """
    ## This path operation shows all travels in the app.

    **- Parameters:** 
    -

    **Returns a json list with all travels in the app, with the following keys:**
    - travel_id: int Primary Key
    - booking_id: int FK
    - Created_at: datetime Field
    - status: bool
                
    """
    travels= db.query(models.Travels).all()
    return travels[skip: skip+limit]


@router.post(
    path="/travels",
    response_model=Travels,
    status_code=status.HTTP_201_CREATED,
    summary="Post a travel",
    tags=["Travels"])
def post_travels(entry_point:Travels,db:Session=Depends(get_db)):
    """
    ## This path operation post a travel in the app.

    **Parameters:**
    travel: Travels

    **Returns a json body with a message:** 
    - message: "Travel Register Successfully"
        
    """
    try:
        travel = models.Travels(booking_id = entry_point.booking_id,
                                created_at = entry_point.created_at,
                                status = entry_point.status)
        db.add(travel)
        db.commit()
        db.refresh(travel)
        return JSONResponse(status_code=201, content={'message': "Travel Register Successfully"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': 'Sorry, there is an error'})