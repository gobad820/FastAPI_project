from datetime import timedelta, datetime
from typing import List

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from domain.todo import todo_schema,todo_crud
from models import Todo
from database import get_db
from starlette import status
router = APIRouter(
    prefix="/api/todo"
)


@router.get("/list",response_model=list[todo_schema.Todo])
def todo_list(db:Session = Depends(get_db)):
    _todo_list = todo_crud.get_todo_list(db)
    return _todo_list


@router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo_crud.delete_todo(db, id)
    return {"message": "Todo deleted successfully"}

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def todo_create(_todo_create:todo_schema.TodoCreate,db:Session=Depends(get_db)):
    todo_crud.create_todo(db=db,todo_create=_todo_create)

@router.get("/detail/{todo_id}",response_model=todo_schema.Todo)
def todo_detail(todo_id: int, db:Session=Depends(get_db)):
    todo=todo_crud.get_todo(db,todo_id=todo_id)
    return todo


@router.get("/todos/{day}", response_model=List[todo_schema.Todo])
def read_todos(day: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    today = datetime.now().date()
    if day == "today":
        start_date = today
        end_date = start_date + timedelta(days=1)
    elif day == "tomorrow":
        start_date = today + timedelta(days=1)
        end_date = start_date + timedelta(days=1)
    elif day == "later":
        start_date = today + timedelta(days=2)
        end_date = start_date + timedelta(days=100)  # or any large number
    else:
        return []

    todos = todo_crud.get_todos_by_date(db, start_date, end_date, skip=skip, limit=limit)
    return todos