from fastapi import FastAPI, Path
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



