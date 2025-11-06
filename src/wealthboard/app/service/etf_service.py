from wealthboard.domain.etf import ETF
from wealthboard.driven.ports.etf_repository import ETFRepository

class ETFService:
    
    def __init__(self, repo: ETFRepository):
        
        self._repo = repo
        
    def fetchAll(self) -> list[ETF]:
        return self._repo.fetchAll().values()
    
    
    def exists(self, ticker: str) -> bool:
        tickers = set(t.lower() for t in self._repo.fetchAll().keys())
        if ticker.lower() in tickers:
            return True
        else:
            return False
        
    def findByTicker(self, ticker: str) -> ETF:
        if self.exists(ticker):
            return self._repo.fetchAll()[ticker.upper()]
        else:
            raise ValueError(f"Ticker {ticker} not found in the repository")