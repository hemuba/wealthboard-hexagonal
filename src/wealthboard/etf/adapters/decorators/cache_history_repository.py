from wealthboard.etf.app.ports.etf_history_repository import ETFHistoryRepository
from wealthboard.etf.domain.etf_history import ETFHistory

class CacheHistoryRepository(ETFHistoryRepository):
    
    def __init__(self, wrapped_repo: ETFHistoryRepository):
        self._wrapped_repo = wrapped_repo
        self._cache: dict[
            tuple[str, str, str],
            dict[tuple, ETFHistory]
        ] = {}
        
    def fetch_by_ticker_and_date(self, ticker: str, from_date: str, to_date: str) -> dict[tuple, ETFHistory]:

        key = (ticker.upper(), from_date, to_date)
        
        if key in self._cache:
            print("CACHE HIT!")
            return self._cache[key]
        
        print("CACHE MISS!")
        data = self._wrapped_repo.fetch_by_ticker_and_date(ticker, from_date, to_date)
        self._cache[key] = data
        return data
