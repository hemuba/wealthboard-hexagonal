from wealthboard.etf.app.dto.etf_history_resp_dto import ETFHistoryRespDTO
from wealthboard.etf.app.ports.etf_history_repository import ETFHistoryRepository
from wealthboard.etf.domain.etf_history import ETFHistory
from wealthboard.common.app.ports.price_provider import PriceProvider
from wealthboard.etf.app.dto.etf_history_req_dto import ETFHistoryReqDTO
from wealthboard.etf.app.mapper.etf_mapper import ETFMapper
from decimal import Decimal
from datetime import datetime

class ETFHistoryService:
    
    def __init__(self, repo: ETFHistoryRepository, price_provider: PriceProvider):
        self._repo = repo
        self._price_provider = price_provider
        
    def fetch_by_ticker_and_date(self, ticker: str, from_date: str, to_date:str=None) -> list[ETFHistoryRespDTO]:
        if to_date is None:
           to_date = datetime.today().strftime("%d-%b-%Y").upper()
        
        etfs = sorted(self._repo.fetch_by_ticker_and_date(ticker, from_date, to_date).values(), key=lambda e: (e.data, e.ticker))
        return [ETFMapper.history_to_dto(e) for e in etfs] 
        
        
    def get_temporal_series(self, ticker:str, from_date:str, to_date:str=None) -> list[float]:
        data = self.fetch_by_ticker_and_date(ticker, from_date, to_date)
        temporal_series = [t.close_price for t in data]
        return temporal_series
    

            
        