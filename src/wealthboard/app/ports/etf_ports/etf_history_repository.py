from abc import ABC, abstractmethod

class ETFHistoryRepository(ABC):
    
    @abstractmethod
    def fetchByTickerFromDate(self, ticker:str, from_date: str):
        """Returns all the ETF and their historical statistics"""