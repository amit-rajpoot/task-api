from fastapi import FastAPI
from app.db.database import engine
from app.models import model
from app.endpoints import auth, tasks

# create DB tables
model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Task Manager")

app.include_router(auth.router)
app.include_router(tasks.router)