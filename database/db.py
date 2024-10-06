from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import DB_HOST, DB_NAME, DB_PASS, DB_USER, DB_PORT

engine = create_async_engine(f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# async def get_async_session():
#     async with async_session_maker() as session:
#         yield session
