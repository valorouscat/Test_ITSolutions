import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

from db import models
from db.database import engine
from app import endpoints, auth


# logging
logging.getLogger().name = __name__
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)-14s - %(levelname)-8s - %(message)s')


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(endpoints.router)
app.include_router(auth.router)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    logging.exception("Unhandled server extencion")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config="log_conf.yaml" )