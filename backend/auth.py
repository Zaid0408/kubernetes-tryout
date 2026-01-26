from fastapi import APIRouter, HTTPException
from jose import jwt 
from datetime import datetime, timedelta
from api_schema import UserLogin, LoginResponse
import json

router=APIRouter(prefix="/auth")


SECRET_KEY="BIG_SECRET"
EXPIRY_IN_MINS=1440
ALGORITHM="HS256"

@router.post("/login", response_model=LoginResponse)
async def login(user:UserLogin):
    with open("user-password.json") as file:
        users=json.load(file)
        
    for u in users:
        if u["username"]==user.username and u["password"]==user.password:
            token=generate_token(user.username)
            return {"token":token}
    raise HTTPException(status_code=401,detail="Invalid username or password")


def generate_token(username:str):
    expiry=datetime.utcnow()+ timedelta(minutes=EXPIRY_IN_MINS)
    payload={"username":username,"exp":expiry.timestamp()}
    access_token=jwt.encode(payload,SECRET_KEY,ALGORITHM)
    return access_token