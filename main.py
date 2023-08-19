from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.database import get_write_session
from app.core.config import WRITE_DATABASE_URL

app = FastAPI()

app.include_router(api_router, prefix="/api")

# 데이터베이스 연결 초기화 및 종료 설정
@app.on_event("startup")
async def startup_db():
    # 데이터베이스 연결 초기화
    get_write_session().configure(bind=WRITE_DATABASE_URL)

@app.on_event("shutdown")
async def shutdown_db():
    # 데이터베이스 연결 종료
    get_write_session().remove()