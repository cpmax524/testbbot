from .celery import app
from app.services.scoring_engine import ScoringEngine

@app.task
def calculate_score_for_token(token_address):
    """
    Calculates the Athena Score for a given token.
    """
    scoring_engine = ScoringEngine()
    score = scoring_engine.calculate_score(token_address)
    return score
