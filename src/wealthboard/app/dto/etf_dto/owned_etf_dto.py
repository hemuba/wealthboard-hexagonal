from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class OwnedETFDTO:
    ticker: str
    no_of_shares: float
    p_price: float