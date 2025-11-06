from wealthboard.driven.ports.owned_etf_repository import OwnedETFRepository
from wealthboard.domain.owned_etf import OwnedETF

class OwnedETFService:

    def __init__(self, repo: OwnedETFRepository):
        
        self._repo = repo
        
    def fetchAll(self) -> list[OwnedETF]:
        return self._repo.fetchAll().values()
    
    def findByTicker(self, ticker: str) -> OwnedETF:
        tickers = set(t.lower() for t in self._repo.fetchAll().keys())
        if ticker.lower() in tickers:
            return self._repo.fetchAll()[ticker.upper()]
        else:
            raise ValueError(f"Ticker {ticker} not found in the repository")
        
    def addEtf(self, etf:OwnedETF):
        self._repo.addEtf(etf)