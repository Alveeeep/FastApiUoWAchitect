from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all_breeds(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all_by_filter(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def edit_one(self, id: int, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].read_model() for row in res.all()]
        return res

    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar_one().read_model()
        return res

    async def delete_one(self, id: int) -> int:
        stmt = delete(self.model).filter_by(id=id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_all_breeds(self):
        stmt = select(self.model.description)
        res = await self.session.execute(stmt)
        return list(set(res.scalars().all()))

    async def find_all_by_filter(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = [row[0].read_model() for row in res.all()]
        return res


