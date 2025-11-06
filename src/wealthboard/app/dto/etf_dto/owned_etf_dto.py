from dataclasses import dataclass

@dataclass(frozen=True)
class OwnedETFDTO:
    ticker: str
    no_of_shares: float
    p_price: float
    c_price: float