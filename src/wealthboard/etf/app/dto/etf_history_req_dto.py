from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True, slots=True)
class ETFHistoryReqDTO:
    data: datetime
    ticker: str
    open_price: float
    close_price: float
    volume: int