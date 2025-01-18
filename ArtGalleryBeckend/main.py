# osnovna FastAPI aplikacija; provjera: uvicorn main:app --reload
from fastapi import FastAPI
from user_models import User
from crud_operations import create_user

app = FastAPI()

@app.post("/users/")
async def add_user(user: User):
    response = create_user(user.dict())
    return response


