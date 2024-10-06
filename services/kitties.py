from schemas.kitties import KittieDTO
from utils.unitofwork import IUnitOfWork


class KittiesService:
    async def add_kittie(self, uow: IUnitOfWork, kittie: KittieDTO):
        kittie_dict = kittie.model_dump()
        async with uow:
            kittie_id = await uow.kitties.add_one(kittie_dict)
            await uow.commit()
            return kittie_id

    async def get_kitties(self, uow: IUnitOfWork):
        async with uow:
            kitties = await uow.kitties.find_all()
            return kitties

    async def get_kittie(self, uow: IUnitOfWork, kittie_id: int):
        async with uow:
            kittie = await uow.kitties.find_one(id=kittie_id)
            return kittie

    async def get_all_breeds(self, uow: IUnitOfWork):
        async with uow:
            breeds = await uow.kitties.find_all_breeds()
            return breeds

    async def edit_kittie(self, uow: IUnitOfWork, kittie_id: int, kittie: KittieDTO):
        kitties_dict = kittie.model_dump()
        async with uow:
            await uow.kitties.edit_one(kittie_id, kitties_dict)
            await uow.commit()

    async def delete_kittie(self, uow: IUnitOfWork, kittie_id: int):
        async with uow:
            await uow.kitties.delete_one(id=kittie_id)
            await uow.commit()

    async def get_kitties_by_breed(self, uow: IUnitOfWork, breed: str):
        async with uow:
            kitties = await uow.kitties.find_all_by_filter(description=breed)
            return kitties
