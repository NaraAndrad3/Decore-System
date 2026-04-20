from fastapi import FastAPI
import models
from database import engine

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Marmoraria API")

@app.get("/")
def read_root():
    return {"status": "Marmoraria System Online", "version": "0.1.0-MVP"}