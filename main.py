from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class Names(BaseModel):
    name: str

@app.get("/")
def index():
    return {"key": "value"}

@app.get("/name")
def getAllNames():
    return db

@app.post("/name/")
def postName(name: Names):
    db.append(name.dict())
    return db[-1]

@app.delete("/name/{number}")
def deleteName(number: int):
    db.pop(number)
    return {}