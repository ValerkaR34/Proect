from  pydantic import  BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[int]
    login: str
    password: str
    post_id: int

class Resourses(BaseModel):
      id: Optional[int]
      price: int
      date_time: datetime
      view: str


class Personal(BaseModel):
    id: Optional[int]
    wage: str
    chart: str
    post_id: int
    rating: int
    salary: int
    name: str
    surname: str


class Extraction_points(BaseModel):
    id: Optional[int]
    status: str
    condition: str
    Firm_Id: int


class Firms(BaseModel):
    id: Optional[int]
    Name: str
    Rights: Optional[str]


