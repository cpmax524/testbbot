from pydantic import BaseModel
from datetime import datetime

class TokenBase(BaseModel):
    symbol: str
    name: str

class TokenCreate(TokenBase):
    pass

class Token(TokenBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    telegram_id: int

class User(UserBase):
    id: int
    telegram_id: int
    tokens: list[Token] = []

    class Config:
        orm_mode = True

class ScoreBase(BaseModel):
    score: float

class ScoreCreate(ScoreBase):
    timestamp: datetime

class Score(ScoreBase):
    id: int
    timestamp: datetime
    token_id: int

    class Config:
        orm_mode = True
