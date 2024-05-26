from pydantic import BaseModel, field_validator

import datetime


class Todo(BaseModel):
    id: int
    content: str | None = None
    due_date: datetime.datetime | None = datetime.datetime.today()


class TodoCreate(BaseModel):
    content: str
    due_date: datetime.datetime | None = datetime.datetime.today()

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
