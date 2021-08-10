from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
    isOver: bool
    date: str