from .base import MySqlBaseRepository
from ...models import Message, MessageCreate


class MessagesRepository(MySqlBaseRepository[Message, MessageCreate]):
    pass
