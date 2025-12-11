# app/main.py
from fastapi import FastAPI
print("app started")
app = FastAPI()

@app.get("/")
def read_root():
    print("read root")
    return {"message": "Hello from FastAPI on ECS!"}


@app.get("/hello/")
def hello():
    return {"message": "Hello"}
