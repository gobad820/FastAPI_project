from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote



POSTGRES_USER = "gimsanghae"
POSTGRES_PASSWORD = quote("Rlatld147@@@") # 패스워드에 특수문자가 있으므로 quote 함수로 인코딩
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
POSTGRES_DB = "todo"
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# create_engine을 통해 connection pool 생성 가능, connection pool은 DB에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가면서 사용
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# DB접속 위한 클래스, autocommit=False로 설정하면 데이터 변경시 commit을 해야만 실제 저장이 된다.
# autocommit=False시 롤백 가능하지만 True면 rollback 불가능 왜?
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# @contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
