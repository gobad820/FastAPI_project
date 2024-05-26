from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from database import get_db
from domain.question import question_schema, question_crud

# from models import Question

router = APIRouter(
    prefix="/api/question"
)


# response_mode = list[question_schema.Question]은 question_list함수의 리턴값은 Questino 스키마로 구성된 리스트임을 의미한다.
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list
