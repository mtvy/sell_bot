from .base import MySqlBaseRepository
from ...models import LastMonth, LastMonthCreate


class LastMonthsRepository(MySqlBaseRepository[LastMonth, LastMonthCreate]):
    pass
