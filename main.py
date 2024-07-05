from fastapi import FastAPI

# Create a variable “app” and assign it to FastAPI() class
app = FastAPI()

# Create a root path for the application and write the corresponding function for it.
@app.get("/")
def root():
    return {"Welcome": "to JNNCE"}

