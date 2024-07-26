from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from db import crud, schemas
from db.database import get_db
from app.auth import auth_check


logger = logging.getLogger(__name__)

router = APIRouter()

# endpoint to get item by id
@router.get("/get_item/{id}", response_model=schemas.Item)
async def read_item(id: int, db: Session = Depends(get_db), auth: bool = Depends(auth_check)):
    if auth:
        item = crud.get_item_by_id(db, id)
        if item is None:
            logger.info(f"Item not found by id: {id}")
            raise HTTPException(status_code=404, detail="Item not found")
        logger.info(f"Item found: {id}")
        return item
    else:
        logger.info("Access denied")
        raise HTTPException(status_code=401, detail="Access denied", headers={"WWW-Authenticate": "Bearer"})

# endpoint to create item
@router.post("/create_item/", response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(get_db), auth: bool = Depends(auth_check)):
    if auth:
        db_item = crud.create_item(db, item)
        return db_item
    else:
        logger.info("Access denied")
        raise HTTPException(status_code=401, detail="Access denied", headers={"WWW-Authenticate": "Bearer"})