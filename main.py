from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from typing import Optional, List
from database import cars
from fastapi.encoders import jsonable_encoder

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


'''
@app.get("/cars/{id}")
# Path function expects ID as a parameter in the URL path
# The ID passed in URL will be assigned to "id" variable in method definition
def get_car_details_by_id(id = Path(...)):   # ... represents that this field is required
    car = cars.get(id)
    return car
'''

@app.get("/cars/{id}")
# Path function expects ID as a parameter in the URL path
# The ID passed in URL will be assigned to "id" variable in method definition
def get_car_by_id(id: int = Path(...)):
    car = cars.get(id)
    return car


'''
@app.post("/add_cars")
def add_cars(adding_cars: List[Car]):
    min_id = len(cars.values())
    for car in adding_cars:
        cars[min_id] = car
'''

@app.post("/add_cars")
def add_cars(adding_cars: List[Car]):
    min_id = len(cars.values()) + 1
    for car in adding_cars:
        cars[min_id] = car



@app.put("/cars/{id}")
def update_car(id: int, car: Car):
    # get the car details for ID given
    retrieved_car = cars.get(id)
    # retrieved_car will contain car details in dict format
    # Convert it to pydantic model
    # take the dict version from DB, unpack it and put it into Car
    # and create a new pydantic model to assign it to retrieved_car
    retrieved_car = Car(**retrieved_car)
    # Convert pydantic model into dict
    updated_car_details = car.dict()
    # Replace the new values old values
    updated_car_details = retrieved_car.copy(update=updated_car_details)
    # send it back to DB in JSON format. Import jsonable_encoder from fastapi.encoders
    cars[id] = jsonable_encoder(updated_car_details)
    response = {}
    response[id] = cars[id]
    return response