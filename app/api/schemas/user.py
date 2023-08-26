from pydantic import BaseModel, Field


class GetUserListResponseSchema(BaseModel):
    id: int = Field(..., description="id")
    name: str = Field(..., description="name")

    class Config:
        orm_mode = True


class CreateUserRequestSchema(BaseModel):
    name: str = Field(..., description="name")


class CreateUserResponseSchema(BaseModel):
    name: str = Field(..., description="name")

    class Config:
        orm_mode = True