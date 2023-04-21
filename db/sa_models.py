import decimal
import json
from datetime import datetime

from sqlalchemy import inspect, Column, Integer, ForeignKey, DateTime, String, Enum, Boolean, BIGINT, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import declarative_base


__all__ = ("Base", "UserModel", "NextModel", "LastMonthModel")


Base = declarative_base()


class MixinSerializers:
    """should only be used as sa model base"""

    def to_python(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    def as_json(self) -> str:
        return json.dumps(self.to_python())

    def __str__(self):
        return f"<{self.__tablename__}(pk={self.pk})>"  # type: ignore


class UserModel(MixinSerializers, Base):  # type: ignore
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id: int = Column(BIGINT, unique=True, nullable=False)
    username: str = Column(String(100), nullable=True, default="no")
    language: str = Column(String(100), nullable=True, default="no")
    is_subscribe: bool = Column(Boolean, default=True, nullable=False)
    is_banned: bool = Column(Boolean, default=False, nullable=False)
    is_admin: bool = Column(Boolean, default=False, nullable=False)
    is_push_maker: bool = Column(Boolean, default=False, nullable=False)
    is_respondent: bool = Column(Boolean, default=False, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    last_active: datetime = Column(DateTime, default=datetime.utcnow)
   
class MessageModel(MixinSerializers, Base):  # type: ignore
    __tablename__ = "messages"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    time: datetime = Column(DateTime, default=datetime.utcnow)
    message: str = Column(String(4000), nullable=True)
    is_sent: int = Column(Integer, default=0, nullable=False)


class SettingModel(MixinSerializers, Base):  # type: ignore
    __tablename__ = "settings"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    subscribe: bool = Column(Boolean, default=True, nullable=False)


class LastMonthModel(MixinSerializers, Base):  # type: ignore
    __tablename__ = "data_last_month"

    index: int = Column(Integer, primary_key=True, autoincrement=True)
    goods: str = Column(String(1000), nullable=True, default="no")
    count_sku: int = Column(BIGINT, nullable=True)
    count_sku_mov: int = Column(BIGINT, nullable=True)
    count_sku_sale: int = Column(BIGINT, nullable=True)
    percent_sku_sale: float = Column(Float, nullable=True)
    count_sellers: int = Column(BIGINT, nullable=True)
    sellers_sell: int = Column(BIGINT, nullable=True)
    percent_sellers_sell: float = Column(Float, nullable=True)
    percent_repurch_orders: float = Column(Float, nullable=True)
    revenuy_excluding_repurch: str = Column(String(100), nullable=True)
    revenuy_including_repurch: str = Column(String(100), nullable=True)
    potencial_revenue: str = Column(String(100), nullable=True)
    lost_revenue: str = Column(String(100), nullable=True)
    percent_lost_revenue: int = Column(BIGINT, nullable=True)
    order_without_revenue: str = Column(String(100), nullable=True)
    sales_with_revenue: str = Column(String(100), nullable=True)
    remains: str = Column(String(100), nullable=True)
    turnover: float = Column(Float, nullable=True)
    avr_revenue: str = Column(String(100), nullable=True)
    avr_price: int = Column(BIGINT, nullable=True)
    cost_of_sale: str = Column(String(100), nullable=True)
    commiss_wb_with_repurch: str = Column(String(100), nullable=True)
    taxes: str = Column(String(100), nullable=True)
    profit: str = Column(String(100), nullable=True)
    percent_profit_revenue: float = Column(Float, nullable=True)
    percent_profit_cost_of_sale: float = Column(Float, nullable=True)
    percent_profit_cost_of_sale_in: float = Column(Float, nullable=True)
    commission: int = Column(BIGINT, nullable=True)
    avr_count_comments: float = Column(Float, nullable=True)
    avr_rates_evalution: float = Column(Float, nullable=True)
    weight_percent_profit_cost_of_sale: int = Column(BIGINT, nullable=True)
    weight_percent_profit_cost_of_attach: int = Column(BIGINT, nullable=True)
    weight_percent_profit_revenue: int = Column(BIGINT, nullable=True)
    weight_revenue: int = Column(BIGINT, nullable=True)
    weight_percent_sku: float = Column(Float, nullable=True)
    weight_percent_sellers: int = Column(BIGINT, nullable=True)
    weight_ranks: int = Column(BIGINT, nullable=True)
    weight_count_comments: float = Column(Float, nullable=True)
    weight_turnover: int = Column(BIGINT, nullable=True)
    weight_lost_revenue: int = Column(BIGINT, nullable=True)
    weight_total_sum: int = Column(BIGINT, nullable=True)
    rank: int = Column(BIGINT, nullable=True)


class NextModel(MixinSerializers, Base):  # type: ignore
    __tablename__ = "data_next"

    index: int = Column(Integer, primary_key=True, autoincrement=True)
    goods: str = Column(String(1000), nullable=True, default="no")
    count_sku: int = Column(BIGINT, nullable=True)
    count_sku_mov: int = Column(BIGINT, nullable=True)
    count_sku_sale: int = Column(BIGINT, nullable=True)
    percent_sku_sale: float = Column(Float, nullable=True)
    count_sellers: int = Column(BIGINT, nullable=True)
    sellers_sell: int = Column(BIGINT, nullable=True)
    percent_sellers_sell: float = Column(Float, nullable=True)
    percent_repurch_orders: float = Column(Float, nullable=True)
    revenuy_excluding_repurch: str = Column(String(100), nullable=True)
    revenuy_including_repurch: str = Column(String(100), nullable=True)
    potencial_revenue: str = Column(String(100), nullable=True)
    lost_revenue: str = Column(String(100), nullable=True)
    percent_lost_revenue: int = Column(BIGINT, nullable=True)
    order_without_revenue: str = Column(String(100), nullable=True)
    sales_with_revenue: str = Column(String(100), nullable=True)
    remains: str = Column(String(100), nullable=True)
    turnover: float = Column(Float, nullable=True)
    avr_revenue: str = Column(String(100), nullable=True)
    avr_price: int = Column(BIGINT, nullable=True)
    cost_of_sale: str = Column(String(100), nullable=True)
    commiss_wb_with_repurch: str = Column(String(100), nullable=True)
    taxes: str = Column(String(100), nullable=True)
    profit: str = Column(String(100), nullable=True)
    percent_profit_revenue: float = Column(Float, nullable=True)
    percent_profit_cost_of_sale: float = Column(Float, nullable=True)
    percent_profit_cost_of_sale_in: float = Column(Float, nullable=True)
    commission: int = Column(BIGINT, nullable=True)
    avr_count_comments: float = Column(Float, nullable=True)
    avr_rates_evalution: float = Column(Float, nullable=True)
    weight_percent_profit_cost_of_sale: int = Column(BIGINT, nullable=True)
    weight_percent_profit_cost_of_attach: int = Column(BIGINT, nullable=True)
    weight_percent_profit_revenue: int = Column(BIGINT, nullable=True)
    weight_revenue: int = Column(BIGINT, nullable=True)
    weight_percent_sku: float = Column(Float, nullable=True)
    weight_percent_sellers: int = Column(BIGINT, nullable=True)
    weight_ranks: int = Column(BIGINT, nullable=True)
    weight_count_comments: float = Column(Float, nullable=True)
    weight_turnover: int = Column(BIGINT, nullable=True)
    weight_lost_revenue: int = Column(BIGINT, nullable=True)
    weight_total_sum: int = Column(BIGINT, nullable=True)
    rank: int = Column(BIGINT, nullable=True)