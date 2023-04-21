from .base import MySqlBaseRepository
from ...models import Next, NextCreate


class NextsRepository(MySqlBaseRepository[Next, NextCreate]):
    pass
