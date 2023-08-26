from sqlalchemy import Column, Unicode, BigInteger, Boolean, VARCHAR

from app.core.db import Base
from app.core.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(128), nullable=False, unique=True)

