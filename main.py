import asyncio
from typing import List, Any

from aiohttp import ClientSession, TCPConnector

from pytile import async_login


async def get_tiles(email: str, password: str) -> List[Any]:
    response_date = []
    async with ClientSession(connector=TCPConnector(verify_ssl=False)) as session:
        api = await async_login(email, password, session)
        tiles = await api.async_get_tiles()

        for key, tile in tiles.items():
            response_date.append(tile.as_dict())

    return response_date


if __name__ == "__main__":
    response = asyncio.run(get_tiles("rahulbadenkal@gmail.com", "rahul@4900"))
    print(response)
