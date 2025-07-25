from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_telegram_id(db: Session, telegram_id: int):
    return db.query(models.User).filter(models.User.telegram_id == telegram_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(telegram_id=user.telegram_id, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_tokens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Token).offset(skip).limit(limit).all()


def create_user_token(db: Session, token: schemas.TokenCreate, user_id: int):
    db_token = models.Token(**token.dict(), owner_id=user_id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


def get_scores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Score).offset(skip).limit(limit).all()


def create_token_score(db: Session, score: schemas.ScoreCreate, token_id: int):
    db_score = models.Score(**score.dict(), token_id=token_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score
