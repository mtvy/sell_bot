from enum import Enum
from aioinflux import InfluxDBClient, InfluxDBWriteError
from datetime import datetime
import logging


class DBParams:
    STATS_DB   = None
    STATS_HOST = None
    STATS_USER = None
    STATS_PASS = None


async def log(user_id: int, user_lang_code: str, action_name: str):
    data = {
        "measurement": "bot_commands",
        "time": datetime.utcnow(),
        "fields": {"action_name": 1},
        "tags": {
            "user": str(user_id),
            "user_lang_code": user_lang_code,
            "command": action_name
        }
    }
   
    '''
    return
    try:
        async with InfluxDBClient(host='influxdb', db='statsdb',
                                  username='user', password='supersecretuserpassword') as client:
            await client.write(data)
    except InfluxDBWriteError as ex:
        logging.error(f"InfluxDB write error: {str(ex)}")
    '''