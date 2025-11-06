from wealthboard.driven.ports.owned_etf_repository import OwnedETFRepository
from wealthboard.domain.owned_etf import OwnedETF
from wealthboard.driving.ports.price_provider import PriceProvider

class OwnedETFService:

    def __init__(self, repo: OwnedETFRepository, price_provider: PriceProvider):
        
        self._repo = repo
        self._price_provider = price_provider
        
    def fetchAll(self) -> list[OwnedETF]:
        return list(self._repo.fetchAll().values())
    
    def findByTicker(self, ticker: str) -> OwnedETF:
        tickers = set(t.lower() for t in self._repo.fetchAll().keys())
        if ticker.lower() in tickers:
            return self._repo.fetchAll()[ticker.upper()]
        else:
            raise ValueError(f"Ticker {ticker} not found in the repository")
        
    def addEtf(self, etf:OwnedETF):
        self._repo.addEtf(etf)
        
    def getPrice(self) -> dict[str, float]:
        current_prices = {}
        for t in self.fetchAll():
            current_prices[t.ticker] = self._price_provider.get_current_price(t.ticker)
        return current_prices
    
    def get_price_diff(self):
        diffs = {}
        for t in self.fetchAll():
            ticker = t.ticker
            old_price = t.current_price
            diffs[ticker] = self._price_provider.get_current_price(ticker) - old_price
        return diffs