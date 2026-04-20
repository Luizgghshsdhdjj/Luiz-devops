from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/status")
def status():
    return {"status": "ok", "mensagem": "API Luiz funcionando"}

@app.get("/teste")
def teste():
    return {"teste": "G2"}
