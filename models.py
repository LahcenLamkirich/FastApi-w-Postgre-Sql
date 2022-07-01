from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import UUID1, BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id = UUID
    first_name : str 
    last_name : str
    age : int
    gendre: Gender
    role: List[Role]