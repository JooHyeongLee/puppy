from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import scoped_session  # 추가

from app.core.config import READ_ONLY_DATABASE_URL, WRITE_DATABASE_URL

# 데이터베이스 읽기 전용 엔진 생성 함수
def create_read_only_engine():
    return create_engine(READ_ONLY_DATABASE_URL)

# 데이터베이스 쓰기용 엔진 생성 함수
def create_write_engine():
    return create_engine(WRITE_DATABASE_URL)

# 데이터베이스 읽기 전용 세션을 만드는 함수
def get_read_only_session() -> Session:
    engine = create_read_only_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

# 데이터베이스 쓰기용 scoped 세션을 만드는 함수
def get_write_session() -> scoped_session:
    engine = create_write_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return scoped_session(SessionLocal)
