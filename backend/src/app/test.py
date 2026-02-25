from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from app.core.constants import STORAGE_DIR
from app.core.store import Store
from app.exeptions.file_exeptions import FileInvalidExtension
from app.services.load_datasets import load_dataset
import logging

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


@app.get("/load")
def test_get_all_loaded():
    return app.state.store.getAll()


@app.get("/load/{filename}", status_code=200)
def test_load(filename: str):
    try:
        df = load_dataset(filename)
        store_id = app.state.store.set(df)
        return JSONResponse(content={"dataframe_session_id": store_id})

    except FileNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"File {filename} does not exists in Abyss storage"
        )

    except FileInvalidExtension as e:
        raise HTTPException(status_code=415, detail=str(e))
