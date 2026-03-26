from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session
import models
from models import Todos
from database import engine, SessionLocal
from typing import Annotated
from pydantic import BaseModel, Field


app = FastAPI()

models.Base.metadata.create_all(bind = engine)


class TodoRequest(BaseModel):
    title: str = Field(min_length= 3, max_length=100)
    description: str = Field(min_length= 3, max_length=300)
    priority: int = Field(ge=1, le=5)
    completed: bool = False 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
def read_all(db : db_dependency):
    return db.query(Todos).all()


@app.get("/todos/{todo_id}")
async def read_todo(db : db_dependency, todo_id: int = Path(gt=1)):
    res = db.query(Todos).filter(Todos.id == todo_id).first()
    if res is not None:
        return res
    raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/todos")
async def create_todo(db : db_dependency, todo_request: TodoRequest):
    new_todo = Todos(
        title=todo_request.title,
        description=todo_request.description,
        priority=todo_request.priority,
        completed=todo_request.completed
    )
    db.add(new_todo)
    db.commit()
    return new_todo


@app.put("/todos/{todo_id}")
async def update_todo(db : db_dependency, todo_id : int, todo_upd : TodoRequest):
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    
    todo.title = todo_upd.title
    todo.description = todo_upd.description
    todo.priority = todo_upd.priority
    todo.completed = todo_upd.completed
    db.add(todo)
    db.commit()
    return todo

@app.delete("/todos/{todo_id}")
async def delete_todo(db : db_dependency, todo_id : int):
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo is not None:
        db.delete(todo)
        db.commit()
        return {"detail": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
