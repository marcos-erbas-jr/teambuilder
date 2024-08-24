from sqlalchemy import Column, Integer, String
from .bancoDeDados import Base

class Inscricao(Base):
    __tablename__ = "inscricoes"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)