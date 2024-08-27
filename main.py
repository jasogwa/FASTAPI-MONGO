from fastapi import FastAPI
from tests import test_router
from database import init_db

app = FastAPI()


@app.on_event('startup')
async def connect():
    await init_db()

app.include_router(test_router, prefix='/tests')
