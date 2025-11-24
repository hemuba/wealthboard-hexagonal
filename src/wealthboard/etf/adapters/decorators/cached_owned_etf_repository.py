from wealthboard.etf.app.ports.owned_etf_repository import OwnedETFRepository
from wealthboard.etf.domain.owned_etf import OwnedETF

class CachedOwnedETFRepository(OwnedETFRepository):
    
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
    
    def addEtf(self, etf: OwnedETF):
        self._wrapped_repo.addEtf(etf)
        self._cache = None