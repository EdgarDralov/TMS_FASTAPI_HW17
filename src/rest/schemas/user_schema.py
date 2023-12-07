from datetime import datetime
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
import re


class UserListSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: Optional[int]
    email: EmailStr
    password: str
    is_Admin: bool
    created_at: datetime
    update_at: datetime


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int]
    email: EmailStr
    password: str

    @validator('password')
    def validate_password(cls, value):
        pattern = r"^(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:;<>,.?~-])[A-Za-z0-9!@#$%^&*()_+{}|:;<>,.?~-]{8,}$"

        if re.match(pattern, value):
            return value
        raise ValueError('The password must consist of one special character, one number and be 8 characters long.')





