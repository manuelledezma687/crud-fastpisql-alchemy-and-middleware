from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from connections import Base

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True,index=True)
    email = Column(String(30))
    telephone = Column(Integer)
    username = Column(String(20))
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    country = Column(String(20))
    language = Column(String(20))
    user_since = Column(String(50))
    status = Column(Integer)
    
class Bookings(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    destiny = Column(String(20))
    payment_method = Column(String(20))
    amount_of_booking = Column(Integer)
    created_at = Column(String(50))
    status = Column(Integer)
    
class Travels(Base):
    __tablename__ = 'travels'
    travel_id = Column(Integer,primary_key=True,index=True)
    booking_id = Column(Integer, ForeignKey("bookings.booking_id"))
    created_at = Column(String(50))
    status = Column(Integer)
    
class Ratings(Base):
    __tablename__ = 'ratings'
    rating_id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    travel_id = Column(Integer, ForeignKey("travels.travel_id"))
    stars = Column(Integer)
    comments = Column(String(140))
    created_at = Column(String(50))
    status = Column(Integer)
