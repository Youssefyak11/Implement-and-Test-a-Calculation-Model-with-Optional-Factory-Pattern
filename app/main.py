from fastapi import FastAPI

app = FastAPI(title="FastAPI Users + Calculations Module 11")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Module 11 – Calculations modeling"}
