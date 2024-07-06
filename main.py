from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, List
from database import cars

# Car model
class Car(BaseModel):
    make: str
    model: str
    year: int
    price: float
    engine: Optional[str] = "V4"
    autonomous: bool
    sold: List[str]



# Create a variable “app” and assign it to FastAPI() class
app = FastAPI()

# Create a root path for the application and write the corresponding function for it.
@app.get("/")
def root():
    return {"Welcome": "to JNNCE"}

# Get request to fetch all the car details from database
@app.get("/cars")
def get_car_details():
    response= [] # an empty list to store details of all cars
    # convert JSON content DB into a list
    for id, car in list(cars.items()):
        cars_dict = {}
        cars_dict[id] = car
        response.append(cars_dict)
    return response



