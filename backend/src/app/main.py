import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.constants import STORAGE_DIR
from app.core.store import Store

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(name)s: %(message)s")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not STORAGE_DIR.exists():
        STORAGE_DIR.mkdir()
        logger.info(f"Created Abyss-Store directory at {STORAGE_DIR}")
    app.state.store = Store()
    logger.info("Initialized Cache Manager")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def hello():
    return {"message": "Hello world!"}
