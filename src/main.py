from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def Root():
    return {"message": "Hello World"}
