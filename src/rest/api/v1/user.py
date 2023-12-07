from fastapi import APIRouter

from src.core.db import session
from src.core.managers.user_manager import UserManager
from src.rest.schemas.user_schema import UserCreateSchema
router = APIRouter()

@router.get('/users')
def get_users():
    return {'': ''}

@router.post('/users')
def create_user(user: UserCreateSchema):
    return UserManager.create(input_data=user.__dict__, session=session)
