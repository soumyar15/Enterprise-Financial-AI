from fastapi import APIRouter

from security.auth_service import AuthService

router = APIRouter()

service = AuthService()


@router.post("/login")

def login():

    return service.login("admin")