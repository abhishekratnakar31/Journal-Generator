from fastapi import FastAPI
from app.routes import journal


app = FastAPI()
app.include_router(journal.router)

@app.get("/")
def home():
    return {"message": "AI Journal Generator API running"}