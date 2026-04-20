from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():

    return {"message": "Hello World"}


@app.get("/status")
def status():
    return {"status": "ok"} 