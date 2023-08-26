from fastapi import APIRouter, Depends, Query, Header
import gettext
from fastapi.responses import JSONResponse

from app.api.models import User
from app.api.schemas import CreateUserRequestSchema
from app.api.services.user_service import UserService

user_router = APIRouter()

def get_translated_text(lang, text_domain, text_key):
    locale = gettext.translation(text_domain, localedir='locales', languages=[lang])
    locale.install()
    translated_text = locale.gettext(text_key)
    return translated_text

@user_router.get("/{id}")
def get_users(id: int, accept_language: str = Header(default="en")):
    lang = accept_language.split(',')[0].split(';')[0]
    translated_hello = get_translated_text(lang, 'app', 'Hello')
    # Your logic to retrieve user data based on the id
    return JSONResponse(content={"message": f"User with ID {id}", "translated_hello": translated_hello})

@user_router.post("/create")
async def create_user(request: CreateUserRequestSchema):
    await UserService().create_user(**request.dict())

    # Your logic to create a new user using user_service.create_user(user)
    return JSONResponse(content={"message": "User created successfully"})