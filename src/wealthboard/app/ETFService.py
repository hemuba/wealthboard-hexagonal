from wealthboard.domain.ETF import ETF
from wealthboard.driven.ports.ETFRepository import ETFRepository

class ETFService():
    
    def __init__(self, repo: ETFRepository):
        
        self._repo = repo
        
    def fetchAll(self) -> list[ETF]:
        return self._repo.fetchAll().values()
       
        
    
    def findByTicker(self, ticker: str) -> ETF:
        tickers = set(t.lower() for t in self._repo.fetchAll().keys())
        if ticker.lower() in tickers:
            return self._repo.fetchAll()[ticker.upper()]
        else:
            raise ValueError(f"Ticker {ticker} not found in the repository")