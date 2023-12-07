from datetime import datetime
from src.core.db import Base
from sqlalchemy import Column, Integer, DateTime

class AbstractModel(Base):
    __abstract__ = True

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    update_at = Column('update_at', DateTime, default=datetime.now, onupdate=datetime.now)
