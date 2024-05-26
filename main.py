from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.question import question_router
from domain.todo import todo_router
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from database import engine, Base


def create_tables():
    Base.metadata.create_all(bind=engine)


app = FastAPI()

create_tables()  # 데이터베이스 테이블 생성

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(todo_router.router)
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))


@app.get("/")
async def index():
    return FileResponse("frontend/dist/index.html")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
