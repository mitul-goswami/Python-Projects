from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import Field, BaseModel
from typing import Annotated
from models import Todos
from sqlalchemy.orm import Session
from database import SessionLocal

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated [Session, Depends(get_db)]

class TodosRequest(BaseModel):
  title: str = Field(min_length= 3, max_length=100)
  description: str = Field(min_length= 3, max_length=300)
  priority: int = Field(ge=1, le=5)
  completed: bool = False 


@router.get("/read-todos")
async def read_todos(db : db_dependency):
  return db.query('Todos').all()

@router.get("/read-todos/{todo_id}")
async def read_todos_by_id(todo_id : int, db : db_dependency):
  res = db.query('Todos').filter(Todos.id == todo_id).first()
  return res

@router.post("/post-todos")
async def post_todos(post_todo : TodoRequest, db : db_dependency):
  new_todo = Todos (
    title = post_todo.title,
    description = post_todo.description,
    priority = post_todo.priority
    completed = post_todo.priority
  )
  db.add(new_todo)
  db.commit()
  return new_todo

@router.put("/put-todos/{todo_id}")
async def put_todo(todo_id : int, db : db_dependency, todo_request : TodosRequest):
  todo = db.query('Todos').filter(Todos.id == todo_id).first()
  todo.title = todo_request.title
  todo.description = todo_request.description
  todo.priority = todo_request.priority
  todo.completed = todo_request.completed
  db.add(todo)
  db.commit()
  return todo


  
  
