from datetime import datetime
from pydantic import Field

from .base import BaseModelBase, ModelBase
from ..sa_models import NextModel

__all__ = ("Next", "NextCreate")


class NextBase(BaseModelBase):
    __sa_model__ = NextModel

    goods: str
    count_sku: int
    count_sku_mov: int
    count_sku_sale: int
    percent_sku_sale: float
    count_sellers: int
    sellers_sell: int
    percent_sellers_sell: float
    percent_repurch_orders: float
    revenuy_excluding_repurch: str
    revenuy_including_repurch: str
    potencial_revenue: str
    lost_revenue: str
    percent_lost_revenue: int
    order_without_revenue: str
    sales_with_revenue: str
    remains: str
    turnover: float
    avr_revenue: str
    avr_price: int
    cost_of_sale: str
    commiss_wb_with_repurch: str
    taxes: str
    profit: str
    percent_profit_revenue: float
    percent_profit_cost_of_sale: float
    percent_profit_cost_of_sale_in: float
    commission: int
    avr_count_comments: float
    avr_rates_evalution: float
    weight_percent_profit_cost_of_sale: int
    weight_percent_profit_cost_of_attach: int
    weight_percent_profit_revenue: int
    weight_revenue: int
    weight_percent_sku: float
    weight_percent_sellers: int
    weight_ranks: int
    weight_count_comments: float
    weight_turnover: int
    weight_lost_revenue: int
    weight_total_sum: int
    rank: int


class Next(NextBase, ModelBase):
    index: int


class NextCreate(NextBase):
    pass

NextBase.update_forward_refs(**locals())
Next.update_forward_refs(**locals())
NextCreate.update_forward_refs(**locals())