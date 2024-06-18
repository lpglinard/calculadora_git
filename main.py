from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/add/?num1=<num1>&num2=<num2>")
async def say_hello(name: str):
    num1 = int()
    return {"message": f"Hello {name}"}
