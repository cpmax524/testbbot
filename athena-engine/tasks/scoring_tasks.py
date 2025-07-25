from .celery import app
from app.services import scoring_engine
from app import crud, models, schemas
from app.database import SessionLocal

@app.task
def calculate_all_scores():
    """
    Calculates the Athena score for all tokens in the database.
    """
    db = SessionLocal()
    tokens = db.query(models.Token).all()
    for token in tokens:
        score = scoring_engine.calculate_athena_score(token.address, token.chain)
        score_data = schemas.ScoreCreate(
            score=score,
            mvrv_ratio=1.2, # placeholder
            exchange_netflow=-6000, # placeholder
            lth_supply_ratio=0.65, # placeholder
            funding_rates=-0.06 # placeholder
        )
        crud.create_score(db, score_data, token.id)
    db.close()
