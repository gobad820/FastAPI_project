from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    due_date = Column(DateTime, nullable=True)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
