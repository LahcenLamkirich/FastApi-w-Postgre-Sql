from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

db: List[User] = [

    User(
        id=uuid4(),
        first_name="Lahcen",
        last_name="Lamkirich",
        age= 22,
        gendre=Gender.male,
        role=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Nouhaila",
        last_name="Hd",
        age= 21,
        gendre=Gender.female,
        role=[Role.student, Role.admin]
    ),
]


@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get("/users")
def fetch_users():
    return db 
