from wealthboard.etf.app.ports.etf_history_repository import ETFHistoryRepository
from wealthboard.etf.domain.etf_history import ETFHistory
from wealthboard.common.app.ports.price_provider import PriceProvider
from datetime import datetime

class ETFHistoryService:
    
    def __init__(self, repo: ETFHistoryRepository, price_provider: PriceProvider):
        self._repo = repo
        self._price_provider = price_provider
        
    def fetchByTickerFromDate(self, ticker: str, from_date: str, to_date:str=None) -> list[ETFHistory]:
        if to_date is None:
           to_date = datetime.today().strftime("%d-%b-%Y").upper()
        return sorted(list(self._repo.fetchByTickerAndDate(ticker, from_date, to_date).values()), key=lambda x: (x[0], x[1]))
    
    def get_temporal_serie(self, ticker:str, from_date:str, to_date:str=None):
        data = self.fetchByTickerFromDate(ticker, from_date, to_date)
        temporal_serie = [t[3] for t in data]
        return temporal_serie
    

            
        