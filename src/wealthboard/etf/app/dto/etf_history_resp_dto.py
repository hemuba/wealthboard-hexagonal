from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass(frozen=True, slots=True)
class ETFHistoryRespDTO:
    data: datetime
    ticker: str
    open_price: float
    close_price: float
    volume: int