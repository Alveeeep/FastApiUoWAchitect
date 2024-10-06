from sqlalchemy.orm import Mapped, mapped_column
from schemas.kitties import KittieDTO
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Kitties(Base):
    __tablename__ = "kitties"

    id: Mapped[int] = mapped_column(primary_key=True)
    color: Mapped[str]
    age: Mapped[int]
    description: Mapped[str]

    def read_model(self) -> KittieDTO:
        return KittieDTO(
            id=self.id,
            color=self.color,
            age=self.age,
            description=self.description
        )
