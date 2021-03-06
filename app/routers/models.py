from typing import Optional
from pydantic import BaseModel


class UserProfile(BaseModel):
    """profile schema expected in body"""
    name: str
    account_name: Optional[str] = None
    username: str
    # todo, on instantiation, add timestamp

class CreateProfileBody(BaseModel):
    username: str
    password: str
    playername: Optional[str] = None

class UserLoginData(BaseModel):
    username: str
    password: str

class AuthnUserProfile(BaseModel):
    """model used in req body for registering a new profile"""
    player_name: str
    username: str
    password: str
    roles: list

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None