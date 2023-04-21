from pydantic import constr
from .base import BaseModelBase, ModelBase
from ..sa_models import MessageModel
from datetime import datetime
from pydantic import Field


__all__ = ("Message", "MessageCreate")


class MessageBase(BaseModelBase):
    __sa_model__ = MessageModel

    time: datetime = Field(default_factory=datetime.utcnow)
    message: str 
    is_sent: bool = False


class Message(MessageBase, ModelBase):
    id: int

class MessageCreate(MessageBase):
    pass


MessageBase.update_forward_refs(**locals())
Message.update_forward_refs(**locals())
MessageCreate.update_forward_refs(**locals())
