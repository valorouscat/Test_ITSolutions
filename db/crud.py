from sqlalchemy.orm import Session
from . import models, schemas
import logging


logger = logging.getLogger(__name__)


def create_item(db: Session, item: schemas.Item):
    logger.info(f"Creating item: {item}")
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item_by_id(db: Session, id: int):
    logger.info(f"Getting item by id: {id}")
    return db.query(models.Item).filter(models.Item.id == id).first()


