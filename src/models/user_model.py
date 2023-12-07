from sqlalchemy import Column, String, Integer, Boolean

from src.models.abstract_model import AbstractModel


class User(AbstractModel):
    __tablename__ = 'users'

    first_name = Column('first_name', String, nullable=False)
    last_name = Column('last_name', String, nullable=False)
    age = Column('age', Integer, nullable=True)
    email = Column('email', String, unique=True, nullable=False)
    password = Column('password', String, unique=True, nullable=False)
    is_Admin = Column('is_Admin', Boolean, default=False)
