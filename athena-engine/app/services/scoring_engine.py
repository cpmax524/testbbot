from .moralis_service import MoralisService

class ScoringEngine:
    def __init__(self):
        self.moralis_service = MoralisService()

    def calculate_score(self, token_address):
        # This is a placeholder for the actual scoring logic.
        #
        # For now, we will just get the token price and calculate a
        # simple score based on that.

        price_data = self.moralis_service.get_token_price(token_address)
        price = price_data["price"]

        # Simple scoring logic:
        # - If the price is > 150, the score is -5 (bearish).
        # - If the price is < 50, the score is +5 (bullish).
        # - Otherwise, the score is 0 (neutral).

        if price > 150:
            score = -5.0
        elif price < 50:
            score = 5.0
        else:
            score = 0.0

        return {"score": score}
