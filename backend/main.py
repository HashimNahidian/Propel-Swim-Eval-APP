from fastapi import FastAPI
from db import engine, Base
import models

app = FastAPI()

# TEMP: creates tables directly (we'll replace this with Alembic next)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"ok": True}
