import decimal
import os
import configparser
_config = configparser.ConfigParser()
_config.read("config.ini", encoding="utf-8")


def _get_from_config_or_env(section: str, key: str) -> str:
    result = _config[section].get(key)
    if not result:
        result = os.environ[f"{section}:{key}"]
    return result


DEBUG = bool(int(_get_from_config_or_env("default", "debug")))
RUNNING_MODULES = _get_from_config_or_env("default", "running_modules").split()

ALEMBIC_SA_URL = _get_from_config_or_env("db", "alembic_sa_url")
TEST_SA_URL = _get_from_config_or_env("db", "test_sa_url")

SA_URL = _get_from_config_or_env("db", "sa_url")
SA_ECHO = bool(int(_get_from_config_or_env("db", "sa_echo")))

ADMIN_TELEGRAM_TOKEN = _get_from_config_or_env("admin_bot", "telegram_token")
TELEGRAM_TOKEN = _get_from_config_or_env("bot", "telegram_token")

ADMIN_TELEGRAM_ID = int(_get_from_config_or_env("app", "admin_telegram_id"))

REDIS_HOST = _get_from_config_or_env("redis", "host")
REDIS_PORT = int(_get_from_config_or_env("redis", "port"))
REDIS_PASSWORD = _get_from_config_or_env("redis", "password")



channel_id = -1001136057546
# channel_id = -1001803188568


import shelve
# файл может получить суффикс, 
# добавленный низкоуровневой библиотекой
dbs = shelve.open("storage")

#dbs["subscribe"]=0


keywords= {
    "men":["мужская","мужское","мужские","мужчинам"],
    "women":["женское","женское","женщинам"],
    "children":["детская","детское","детей","детям","малышей","малышам"],
}
