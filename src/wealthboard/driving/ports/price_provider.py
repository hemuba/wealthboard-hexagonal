from abc import ABC, abstractmethod

class PriceProvider(ABC):
    
    @abstractmethod
    def get_current_price(self, ticker:str) -> float:
        """Retrieves the current price for the provided ETF(s)"""
        pass