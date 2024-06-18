from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/add/{num1}/{num2}")
async def add(num1: float, num2: float):
    return {"message": f"Hello {num1+num2}"}
