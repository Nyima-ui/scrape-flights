1. [x] revision: uvicorn (command to start server as well), pydantic, decorator, fastapi, imports
2. [x] understand the code in main.py
2. [x] write Fastapi post request 
2. [x] clean the response data
2. [x] refactor the code
2. [x] test and run the api
2. [x] add iata codes
5. [] deploy this backend on render.com
6. [] set up git hub actions cron job
7. [] research & plan backend api to setup price alert
8. [] write backend api 
9. [] test the api


# task 1: revise the code below
```
scrape-flights/
├── app/                # All your FastAPI code lives here
│   ├── __init__.py
│   ├── main.py         # Entry point: Initialize FastAPI app
│   ├── routes.py       # API endpoints (GET /flights, etc.)
│   ├── schemas.py      # Pydantic models for request/response validation
│   └── services/       # The "Brain": Business logic & scraping logic
│       ├── __init__.py
│       └── flight_service.py # Wraps the fast-flights library calls
├── data/               # Local storage for your data.json files
├── .gitignore
├── pyproject.toml      # Managed by uv
├── uv.lock            # Managed by uv
└── README.md
```