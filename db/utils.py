import asyncio
import logging

from sqlalchemy import text


async def wait_for_mysql():
    from db.core import engine
    retries = 10
    while True:
        print(retries)
        try:
            async with engine.begin() as conn:
                await conn.execute(text("SELECT 1"))
            await engine.dispose()
            logging.info("Connected to MYSQL")
            return
        except Exception as e:
            logging.error(f"Waiting for MYSQL ({retries=}): {e}")
            await asyncio.sleep(1)
            retries -= 1
            if retries == 0:
                raise e
