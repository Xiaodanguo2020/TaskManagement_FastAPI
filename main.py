from models import Programmer, Languages
from typing import List

# 1. Import package fastAPI
from fastapi import FastAPI

# 2. Create a FastAPI "instance"
app = FastAPI()

# 3. Write the first endpoint


@app.get("/")  # path operation decorator
async def root():
    return {"message": "Hello World"}

# 3. Write the first endpoint


@app.get("/test")  # path operation decorator
async def root():
    return {"message": "test"}

db: List[Programmer] = [
    Programmer(id=1, name="Dennis Ritchie",
               languages=[Languages.b, Languages.c]),
    Programmer(id=2, name="Brian Wilson Kernighan", languages=[Languages.c]),
    Programmer(id=3, name="James Gosling", languages=[Languages.java]),
    Programmer(id=4, name="Guido van Rossum", languages=[Languages.python]),
    Programmer(id=4, name="Brendan Eich", languages=[Languages.javascript])
]


@app.get("/programmers", response_model=list[Programmer])
async def get_programmers() -> list[Programmer]:
    return db


@app.get("/hi/{name}")
async def say_hi(name):
    return name


@app.get("/programmer/{id}", response_model=Programmer)
async def get_programmer(id: int):
    response = next(
        (programmer for programmer in db if programmer.id == id), None)
    return response


@app.get("/programers", response_model=list[Programmer])
async def get_programmers(skip: int = 0, limit: int = 5) -> list[Programmer]:
    return db[skip:skip+limit]


@app.post("/programmers", response_model=Programmer)
async def register_programmer(programmer: Programmer):
    db.append(programmer)
    return programmer
