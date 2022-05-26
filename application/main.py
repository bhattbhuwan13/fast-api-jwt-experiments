"""FastAPI starter sample
"""
import os

from dotenv import load_dotenv
from fastapi import Body, Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

api_key = os.getenv("API_KEY")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)  # use token authentication


api_key = os.getenv("API_KEY")


def api_key_auth(api_key_user: str = Depends(oauth2_scheme)):
    print(api_key, api_key_user)
    if api_key_user != api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not allowed to send request to the API in absence of a valid key",
        )


app = FastAPI()


@app.get("/protected", dependencies=[Depends(api_key_auth)])
def add_post() -> dict:
    return {"data": "You used a valid API key."}


@app.get("/")
def hello() -> dict:
    return {"data": "Hello World"}
