from typing import List

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from app.api import router

from app.core.middlewares import (
    SQLAlchemyMiddleware,
    ResponseLogMiddleware,
)

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(SQLAlchemyMiddleware),
        Middleware(ResponseLogMiddleware),
    ]
    return middleware

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="puppy",
        description="puppy API",
        version="1.0.0",
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    return app_

app = create_app()
