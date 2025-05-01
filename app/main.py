from fastapi import FastAPI, Depends
from app.adapters.input import fastapi_adapter

app = FastAPI()

app.include_router(
    fastapi_adapter.router,
)
