from pydantic import constr
from .base import BaseModelBase, ModelBase
from ..sa_models import SettingModel
from datetime import datetime
from pydantic import Field


__all__ = ("Setting", "SettingCreate")


class SettingBase(BaseModelBase):
    __sa_model__ = SettingModel

    subscribe: int = 0


class Setting(SettingBase, ModelBase):
    id: int

class SettingCreate(SettingBase):
    pass


SettingBase.update_forward_refs(**locals())
Setting.update_forward_refs(**locals())
SettingCreate.update_forward_refs(**locals())
