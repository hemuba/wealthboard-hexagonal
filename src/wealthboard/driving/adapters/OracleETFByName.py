from wealthboard.driving.ports.ETFByName import ETFByName
from wealthboard.domain.ETF import ETF
from wealthboard.driven.adapters.OracleETFRepository import OracleETFRepository

class OracleETFByName(ETFByName):
    
    def __init__(self, repo: OracleETFRepository):
        
        self._repo = repo
        
    def findByTicker(self, ticker: str) -> ETF:
        tickers = set(t.lower() for t in self._repo.fetchAll().keys())
        if ticker.lower() in tickers:
            return self._repo.fetchAll()[ticker.upper()]
        else:
            raise ValueError(f"Ticker {ticker} not found in the repository")