from typing import List
from app.utils import clean_data
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fast_flights import FlightData, Passengers, Result, get_flights
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "https://fairdrop-sage.vercel.app",
    "http://127.0.0.1:3000",
]

app = FastAPI(
    title="Flight Search API",
    description="Search for flights using Google Flights data.",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FlightRequest(BaseModel):
    origin: str = Field(..., example="DEL")
    destination: str = Field(..., example="IXL")
    date: str = Field(..., example="2026-03-05")


class FlightResponse(BaseModel):
    name: str
    departure: str
    arrival: str
    duration: str
    stops: int | str
    price: str
    airline_logo: str | None = None


class SearchFlightsResponse(BaseModel):
    origin: str
    destination: str
    flights: List[FlightResponse]


AIRLINE_CODES = {
    # Indian Airlines
    "IndiGo": "6E",
    "Air India": "AI",
    "SpiceJet": "SG",
    "Vistara": "UK",
    "Go First": "G8",
    "AirAsia India": "I5",
    "Alliance Air": "9I",
    "Air India Express": "IX",
    # International Airlines
    "Emirates": "EK",
    "Qatar Airways": "QR",
    "Singapore Airlines": "SQ",
    "Thai Airways": "TG",
    "Etihad Airways": "EY",
    "British Airways": "BA",
    "Lufthansa": "LH",
    "Air France": "AF",
    "KLM": "KL",
    "United Airlines": "UA",
    "American Airlines": "AA",
    "Delta Air Lines": "DL",
    "Southwest Airlines": "WN",
    "JetBlue Airways": "B6",
    "Turkish Airlines": "TK",
    "Cathay Pacific": "CX",
    "Japan Airlines": "JL",
    "ANA": "NH",
    "Korean Air": "KE",
    "Qantas": "QF",
    "Air Canada": "AC",
    # Add more as you encounter them
}


def get_airline_logo(airline_name):
    """Get airline logo URL from airline name"""
    code = AIRLINE_CODES.get(airline_name)
    if code:
        return f"https://www.gstatic.com/flights/airline_logos/70px/{code}.png"
    return None


@app.post("/search-flights", response_model=SearchFlightsResponse, tags=["Flights"])
def search_flights(request: FlightRequest):
    try:
        result: Result = get_flights(
            flight_data=[
                FlightData(
                    date=request.date,
                    from_airport=request.origin,
                    to_airport=request.destination,
                )
            ],
            trip="one-way",
            seat="economy",
            passengers=Passengers(adults=1),
            fetch_mode="fallback",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch flights: {e}")

    flights = clean_data(result.flights)
    for flight in flights: 
        flight["airline_logo"] = get_airline_logo(flight["name"])
    return {
        "origin": request.origin,
        "destination": request.destination,
        "flights": flights,
    }


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Flight search API is running",
        "version": "1.0.0",
    }
