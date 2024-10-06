from fastapi import APIRouter, Depends
from typing import Annotated
from schemas.kitties import KittieDTO
from services.kitties import KittiesService
from utils.unitofwork import UnitOfWork, IUnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]

router = APIRouter(
    prefix="/kitties",
    tags=["Kitties"],
)


@router.get("/get_kitties")
async def get_kitties(uow: UOWDep):
    kitties = await KittiesService().get_kitties(uow)
    return kitties


@router.get("/kittie/{id}")
async def get_kittie(uow: UOWDep, id: int):
    kittie = await KittiesService().get_kittie(uow, id)
    return kittie


@router.get("/get_breeds")
async def get_breeds(uow: UOWDep):
    breeds = await KittiesService().get_all_breeds(uow)
    return breeds


@router.get("/get_kitties/{breed}")
async def get_kitties_by_breed(uow: UOWDep, breed: str):
    kitties = await KittiesService().get_kitties_by_breed(uow, breed)
    return kitties


@router.post("/add_kittie")
async def add_kittie(uow: UOWDep, kittie: KittieDTO):
    kittie_id = await KittiesService().add_kittie(uow, kittie)
    return {"kitties_id": kittie_id}


@router.patch("kittie/{id}")
async def edit_kittie(uow: UOWDep, kittie: KittieDTO, id: int):
    await KittiesService().edit_kittie(uow, id, kittie)
    return {"ok": True}


@router.delete("/kittie/{id}")
async def delete_kittie(uow: UOWDep, id: int):
    await KittiesService().delete_kittie(uow, id)
    return {"ok": True}
