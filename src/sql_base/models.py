from  pydantic import  BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id:Optional[int]
    login: str
    password: str
    phone_number: str
    reg_date: Optional[datetime]


class Resourses(BaseModel):
      id: Optional
      prise: str
      date_time: datetime
      view: str


class Personal(BaseModel):
    id: Optional
    wage: str
    chart: str
    post: str
    rating: str
    name: str
    surname: str

class Extraction_points(BaseModel):
    id: Optional
    status: str
    type_id: int
    condition: str
    Firm_id: int

class Firm(BaseModel):
    id: Optional
    Name: str
    Rights: Optional[str]


