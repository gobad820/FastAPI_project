from models import Todo
from dateutil.parser import parse
from sqlalchemy.orm import Session
from domain.todo.todo_schema import TodoCreate
from datetime import datetime


def get_todo_list(db: Session):
    todo_list = db.query(Todo).order_by(Todo.due_date.asc()).all()
    return todo_list


def delete_todo(db: Session, id: int):
    todo_item = db.query(Todo).filter(Todo.id == id).first()
    if todo_item is not None:
        db.delete(todo_item)
        db.commit()


def create_todo(db: Session, todo_create: TodoCreate):
    # due_date = parse(todo_create.due_date)
    db_todo = Todo(content=todo_create.content, due_date=todo_create.due_date)
    db.add(db_todo)
    db.commit()


def get_todo(db: Session, todo_id: int):
    todo = db.query(Todo).get(todo_id
                              )
    return todo
