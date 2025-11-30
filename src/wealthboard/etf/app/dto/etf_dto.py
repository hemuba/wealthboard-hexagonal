from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ETFDTO:
    ticker: str
    company_name: str
    exchange: str
    theme: str
    