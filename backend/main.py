from fastapi import FastAPI

app = FastAPI(title="Marmoraria API")

@app.get("/")
def read_root():
    return {"status": "Marmoraria System Online", "version": "0.1.0-MVP"}