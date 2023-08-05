import datetime
from pydantic import BaseModel, Field

class BookingCreate(BaseModel):
    booking_id: int

class Booking(BookingCreate):
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str = Field(max_length=12)

class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True

class RoomCreate(BaseModel):
    room_id: int

class Room(RoomCreate):
    room_name: str = Field(max_length=12)
    capacity: int

    class Config:
        orm_mode = True
