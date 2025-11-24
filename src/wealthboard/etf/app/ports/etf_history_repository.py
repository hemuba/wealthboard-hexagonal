from abc import ABC, abstractmethod
from wealthboard.etf.domain.etf_history import ETFHistory

class ETFHistoryRepository(ABC):
    
    @abstractmethod
    def fetchByTickerFromDate(self, ticker:str, from_date: str) -> dict[tuple, ETFHistory]:
        """Returns all the ETF and their historical statistics"""