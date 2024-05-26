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
