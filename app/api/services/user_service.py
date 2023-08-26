from app.api.models.user import User
from app.core.db.transactional import Transactional, session
from app.api.schemas.user import CreateUserRequestSchema


class UserService:
    def __init__(self):
        ...

    @Transactional()
    async def create_user(
            self, name: str
    ) -> None:
        user = User(name=name)
        session.add(user)

    def get_users(self, skip: int = 0, limit: int = 10):
        # 사용자 목록 조회 로직
        return []

    def get_user(self, user_id: int):
        # 사용자 단일 조회 로직
        return None

    def update_user(self, user_id: int, user: User):
        # 사용자 업데이트 로직
        return None

    def delete_user(self, user_id: int):
        # 사용자 삭제 로직
        return None