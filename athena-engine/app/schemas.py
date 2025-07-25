from pydantic import BaseModel
import datetime

class TokenBase(BaseModel):
    symbol: str
    address: str
    chain: str

class TokenCreate(TokenBase):
    pass

class Token(TokenBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    telegram_id: int
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    tokens: list[Token] = []

    class Config:
        orm_mode = True

class ScoreBase(BaseModel):
    score: float
    mvrv_ratio: float
    exchange_netflow: float
    lth_supply_ratio: float
    funding_rates: float

class ScoreCreate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int
    token_id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
