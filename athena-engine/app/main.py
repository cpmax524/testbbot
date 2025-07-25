from fastapi import FastAPI
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    db = SessionLocal()
    db_user = crud.create_user(db, user)
    db.close()
    return db_user

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int):
    db = SessionLocal()
    db_user = crud.get_user(db, user_id)
    db.close()
    return db_user

@app.post("/tokens/", response_model=schemas.Token)
def create_token(token: schemas.TokenCreate):
    db = SessionLocal()
    db_token = crud.create_token(db, token)
    db.close()
    return db_token

@app.get("/tokens/{token_id}", response_model=schemas.Token)
def read_token(token_id: int):
    db = SessionLocal()
    db_token = crud.get_token(db, token_id)
    db.close()
    return db_token

@app.post("/scores/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate):
    db = SessionLocal()
    db_score = crud.create_score(db, score)
    db.close()
    return db_score

@app.get("/scores/{score_id}", response_model=schemas.Score)
def read_score(score_id: int):
    db = SessionLocal()
    db_score = crud.get_score(db, score_id)
    db.close()
    return db_score
