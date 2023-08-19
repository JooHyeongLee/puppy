from fastapi import APIRouter, Request
import gettext
from fastapi.responses import JSONResponse


router = APIRouter()

def get_translated_text(lang, text_domain, text_key):
    locale = gettext.translation(text_domain, localedir='locales', languages=[lang])
    locale.install()
    translated_text = locale.gettext(text_key)
    return translated_text

@router.get("/")
def get_users(request: Request):
    accept_language = request.headers.get("accept-language", "en")  # 브라우저 언어 가져오기
    lang = accept_language.split(',')[0].split(';')[0]  # 첫 번째 언어 선택
    translated_hello = get_translated_text(lang, 'app', 'Hello')

    return JSONResponse(content={"message": "List of users", "translated_hello": translated_hello})


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"User {user_id}"}