from wealthboard.app.ports.etf_ports.owned_etf_repository import OwnedETFRepository
from wealthboard.domain.etf.owned_etf import OwnedETF
from wealthboard.app.ports.price_provider import PriceProvider

class OwnedETFService:

    def __init__(self, repo: OwnedETFRepository, price_provider: PriceProvider):
        
        self._repo = repo
        self._price_provider = price_provider
        
    def fetchAll(self) -> list[OwnedETF]:
        etfs = list(self._repo.fetchAll().values())
        for e in etfs:
            e.current_price = self._price_provider.get_current_price(e.ticker)
        return etfs

    def findByTicker(self, ticker: str) -> OwnedETF:
        owned = self._repo.fetchAll().get(ticker.upper())
        if not owned:
            raise ValueError(f"Ticker {ticker} not found in the repository")
        owned.current_price = self._price_provider.get_current_price(owned.ticker)
        return owned
            
        
    def addEtf(self, etf:OwnedETF):
        self._repo.addEtf(etf)
        
    def getPrice(self) -> dict[str, float]:
        current_prices = {}
        for t in self.fetchAll():
            current_prices[t.ticker] = self._price_provider.get_current_price(t.ticker)
        return current_prices

    
    def get_percentage_return(self):
        current_percentage_return = {}
        for t in self.fetchAll():
            current_percentage_return[t.ticker] = round((t.current_price / t.purchase_price - 1) * 100, 2) 
        return dict(sorted(current_percentage_return.items(), key=lambda x: x[1], reverse=True))