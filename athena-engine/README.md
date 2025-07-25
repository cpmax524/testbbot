# Athena

Athena is a sophisticated, real-time, on-chain decision engine designed for cryptocurrency traders and investors who want to leverage the deep insights of blockchain data. The system moves beyond simple price analysis to provide a multi-faceted, quantitative assessment of any supported crypto asset.

## How to Run Locally

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/athena-engine.git
    cd athena-engine
    ```

2.  **Set up the environment variables:**

    Create a `.env` file in the `athena-engine` directory and add the following:

    ```
    MORALIS_API_KEY=your_moralis_api_key
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    DATABASE_URL=postgresql://user:password@db/athena
    ```

3.  **Run the application:**

    ```bash
    docker-compose up --build
    ```

## How It Works

### Scoring Engine

The heart of Athena is its quantitative scoring model. The scoring engine calculates the "Athena Score" based on a variety of on-chain metrics, including:

*   **MVRV Ratio:** Measures the market value to realized value of a token.
*   **Exchange Netflow:** Tracks the net amount of a token moving in or out of exchanges.
*   **LTH Supply Ratio:** The ratio of long-term holder supply to the total supply.
*   **Funding Rates:** The cost to hold a long or short position in a perpetual futures market.

### Telegram Bot

The Telegram bot provides an interface for users to interact with the Athena engine. Users can add tokens to their watchlist and receive real-time alerts based on the Athena Score.

### API

The FastAPI application provides a RESTful API for interacting with the Athena engine. The API can be used to:

*   Create and manage users and their watchlists.
*   Get the latest Athena Score for a token.
*   Get historical scores for a token.

## Project Structure

```
athena-engine/
├── app/                  # Main application source code
│   ├── __init__.py
│   ├── main.py           # FastAPI application entry point
│   ├── crud.py           # Database operations (Create, Read, Update, Delete)
│   ├── database.py       # Database connection and session management
│   ├── models.py         # SQLAlchemy ORM models (Users, Tokens, Scores)
│   ├── schemas.py        # Pydantic schemas for data validation (API requests/responses)
│   └── services/         # Business logic
│       ├── __init__.py
│       ├── moralis_service.py   # Logic for interacting with Moralis API
│       ├── derivatives_service.py # Logic for derivatives data
│       └── scoring_engine.py  # The core scoring algorithm
│
├── bot/                    # Telegram bot specific code
│   ├── __init__.py
│   ├── main.py             # Main bot entry point
│   ├── handlers.py         # Handlers for different Telegram commands (/start, /add_token)
│   └── messages.py         # Formatted message templates sent to users
│
├── tasks/                  # Celery background tasks
│   ├── __init__.py
│   ├── celery.py           # Celery app configuration
│   └── scoring_tasks.py    # The periodic task that calculates scores for all tokens
│
├── tests/                  # Unit and integration tests
│
├── .env                    # Environment variables (API keys, DB credentials)
├── docker-compose.yml      # Docker configuration for local development
├── Dockerfile              # Dockerfile for building the application image
└── requirements.txt        # Python project dependencies
```
