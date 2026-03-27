# models.py
from pydantic import BaseModel

class TodoItemBase(BaseModel):
    title: str
    description: str

class TodoItem(TodoItemBase):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True

class CreateTodoItem(BaseModel):
    title: str
    description: str

class UpdateTodoItem(BaseModel):
    title: str | None
    description: str | None
    completed: bool | None

# settings.py
from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    database_url: str = "sqlite:///todo.db"

    class Config:
        env_file = ".env"

# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware
from app.routes import todo_router
from app.settings import Settings
from database import get_db

app = FastAPI(
    title="TODO APP",
    description="TODO APP API",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router, prefix="/todo", tags=["TODO"])

@app.exception_handler(Exception)
async def except_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": str(exc)})

# crud.py
from app.models import TodoItem
from sqlalchemy.orm import Session
from sqlalchemy import func

def create_todo(db: Session, item: TodoItem):
    db_todo = TodoItem(
        title=item.title,
        description=item.description,
        completed=item.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo(db: Session, id: int):
    db_todo = db.query(TodoItem).filter(TodoItem.id == id).first()
    return db_todo

def update_todo(db: Session, item: TodoItem):
    db_todo = get_todo(db, item.id)
    if db_todo:
        db_todo.title = item.title
        db_todo.description = item.description
        db_todo.completed = item.completed
        db.commit()
        return db_todo
    return None

def delete_todo(db: Session, id: int):
    db_todo = get_todo(db, id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return None

# database.py
from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from .settings import Settings

# Create an engine to our database
engine = create_engine(Settings().database_url)

# Create an instance of Base
Base = declarative_base()

# Initialize the database
Base.metadata.create_all(bind=engine)

# get_db.py
from .database import engine

def get_db():
    connection = engine.connect()
    return connection

# routes.py
from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import Depends
from pydantic import BaseModel
from app import crud, schemas
from app import views
from app.database import get_db

router = APIRouter(
    prefix="/todo",
    tags=["TODO"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.get("/", response_model=list[schemas.TodoItem])
def get_todos(db: object = Depends(get_db)):
    connection = db.connect()
    query = select([schemas.TodoItem])
    result = connection.execute(query)
    return result.fetchall()

@router.post("/", response_model=schemas.TodoItem)
def create_todos(db: object = Depends(get_db), item: schemas.CreateTodoItem = Depends()):
    connection = db.connect()
    crud.create_todo(connection, item)
    connection.close()
    return item

@router.put("/{id}", response_model=schemas.TodoItem)
def update_todos(db: object = Depends(get_db), id: int = 1, item: schemas.UpdateTodoItem = Depends()):
    connection = db.connect()
    try:
        crud.update_todo(connection, id, item)
    except:
        raise HTTPException(status_code=500, detail=f"error updating {id}")
    connection.close()
    return item

@router.delete("/{id}", response_model=schemas.TodoItem)
def delete_todos(db: object = Depends(get_db), id: int = 1):
    connection = db.connect()
    try:
        crud.delete_todo(connection, id)
    except:
        raise HTTPException(status_code=500, detail=f"error deleting {id}")
    connection.close()
    return id

# views.py
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from sqlalchemy.orm import Session
from app import crud
from app.models import CreateTodoItem

def get_todo(db: Session = Depends(get_db)):
    connection = db.connect()
    query = select([schemas.TodoItem])
    result = connection.execute(query)
    return result.fetchall()

def create_todo(db: Session = Depends(get_db), item: CreateTodoItem = Depends()):
    crud.create_todo(db, item)
    return item

def update_todo(db: Session = Depends(get_db), id: int = 1, item: CreateTodoItem = Depends()):
    crud.update_todo(db, id, item)
    return id

def delete_todo(db: Session = Depends(get_db), id: int = 1):
    crud.delete_todo(db, id)
    return id