from src.core.managers.base_managers import BaseManager
from src.models.user_model import User


class UserManager(BaseManager):
    table = User
