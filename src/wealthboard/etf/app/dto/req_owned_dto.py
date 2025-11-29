from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True, slots=True)
class ReqOwnedDTO:
    ticker: str
    no_of_shares: Decimal
    purchase_price: Decimal