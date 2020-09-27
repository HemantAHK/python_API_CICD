from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def Root():
    return {"message": "Hello World"}
