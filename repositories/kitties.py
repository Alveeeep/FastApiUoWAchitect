from models.kitties import Kitties
from utils.repository import SQLAlchemyRepository


class KittiesRepository(SQLAlchemyRepository):
    model = Kitties
