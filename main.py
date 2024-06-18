from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/multiply/{num1}/{num2}")
async def multiplicacao(num1: int, num2: int):
    result = num1 * num2
    return {"result": f"{result}"}
