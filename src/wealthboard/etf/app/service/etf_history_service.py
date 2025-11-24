from wealthboard.etf.app.ports.etf_history_repository import ETFHistoryRepository
from wealthboard.etf.domain.etf_history import ETFHistory
from wealthboard.common.app.ports.price_provider import PriceProvider

class ETFHistoryService:
    
    def __init__(self, repo: ETFHistoryRepository, price_provider: PriceProvider):
        self._repo = repo
        self._price_provider = price_provider
        
    def fetchByTickerFromDate(self, ticker: str, date: str ) -> list[ETFHistory]:
        return sorted(list(self._repo.fetchByTickerFromDate(ticker, date).values()), key=lambda x: (x[0], x[1]))
    
    def get_temporal_serie(self, ticker:str, date:str):
        data = self.fetchByTickerFromDate(ticker, date)
        temporal_serie = [t[3] for t in data]
        return temporal_serie
    
    def calculate_percentage_return(self, ticker:str, date: str) -> list[float]:
        pct_returns = []
        temporal_serie = self.get_temporal_serie(ticker, date)
        for i in range(1, len(temporal_serie)):
            pct_returns.append(temporal_serie[i] / temporal_serie[i-1] - 1)
        return pct_returns
            
        