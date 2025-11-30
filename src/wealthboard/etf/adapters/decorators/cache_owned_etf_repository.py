from wealthboard.etf.app.ports.owned_etf_repository import OwnedETFRepository
from wealthboard.etf.domain.owned_etf import OwnedETF

class CacheOwnedETFRepository(OwnedETFRepository):
    
    def __init__(self, wrapped_repo:OwnedETFRepository):
        self._wrapped_repo = wrapped_repo
        self._cache: dict[str, OwnedETF] | None = None
        
    def fetchAll(self) -> dict[str, OwnedETF]:
        if self._cache is not None:
            print("CACHE HIT!")
            return self._cache
        
        data = self._wrapped_repo.fetchAll()
        self._cache = data
        print("CACHE MISS!")
        return data
    
    def findByTicker(self, ticker: str) -> OwnedETF:

        if self._cache is not None:
            etf = self._cache.get(ticker.upper())
            if etf is None:
                raise ValueError(f"Ticker {ticker.upper()} not found in your wallet")
            return etf
        
        etf = self._wrapped_repo.findByTicker(ticker)
        return etf
    

    def addEtf(self, etf: OwnedETF):
        self._wrapped_repo.addEtf(etf)
        self._cache = None