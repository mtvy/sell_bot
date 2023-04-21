from .base import MySqlBaseRepository
from ...models import Setting, SettingCreate


class SettingsRepository(MySqlBaseRepository[Setting, SettingCreate]):
    pass
