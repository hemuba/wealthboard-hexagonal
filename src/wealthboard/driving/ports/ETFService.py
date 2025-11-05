from wealthboard.domain.ETF import ETF
from abc import ABC, abstractmethod


class ETFService(ABC):
    """Contract to access ETF data by name (DB, JSON, CSV, API, ecc.)"""
     
    @abstractmethod   
    def findByTicker(self, ticker:str) -> ETF:
        """Retrieves one ETF by providing its Ticker"""
        pass