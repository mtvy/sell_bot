from pydantic import constr
from .base import BaseModelBase, ModelBase
from ..sa_models import UserModel
from datetime import datetime
from pydantic import Field


__all__ = ("User", "UserCreate")


class UserBase(BaseModelBase):
    __sa_model__ = UserModel

    telegram_id: int
    username: str = "no"
    language: str = "no"
    is_subscribe: bool = True
    is_banned: bool = False
    is_admin: bool = False
    is_push_maker: bool = False
    is_respondent: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_active: datetime = Field(default_factory=datetime.utcnow)

class User(UserBase, ModelBase):
    id: int

    def get_ref_url(self, bot_username: int):
        return f"https://t.me/{bot_username}?start={self.id}"


class UserCreate(UserBase):
    pass


UserBase.update_forward_refs(**locals())
User.update_forward_refs(**locals())
UserCreate.update_forward_refs(**locals())
