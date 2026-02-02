from typing import List
from app.utils import clean_data
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fast_flights import FlightData, Passengers, Result, get_flights


app = FastAPI(
    title="Flight Search API",
    description="Search for flights using Google Flights data.",
    version="1.0.0",
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


class SearchFlightsResponse(BaseModel):
    origin: str
    destination: str
    flights: List[FlightResponse]


@app.post("/search-flights", response_model=SearchFlightsResponse)
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
