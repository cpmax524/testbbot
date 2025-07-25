from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    tokens = relationship("Token", back_populates="owner")

class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    address = Column(String, unique=True, index=True)
    chain = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tokens")
    scores = relationship("Score", back_populates="token")

class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    token_id = Column(Integer, ForeignKey("tokens.id"))
    score = Column(Float)
    mvrv_ratio = Column(Float)
    exchange_netflow = Column(Float)
    lth_supply_ratio = Column(Float)
    funding_rates = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    token = relationship("Token", back_populates="scores")
