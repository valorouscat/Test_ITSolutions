from pydantic import BaseModel


class Item(BaseModel):
    title: str
    id: int
    author: str
    views: int
    position: int

    class Config:
        orm_mode = True

