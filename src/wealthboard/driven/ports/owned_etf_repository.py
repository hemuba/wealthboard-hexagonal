from abc import ABC, abstractmethod
from wealthboard.domain.owned_etf import OwnedETF

class OwnedETFRepository(ABC):
    
    @abstractmethod
    def fetchAll(self):
        """Returns all the Owned ETF"""
    pass


    @abstractmethod
    def addEtf(self, etf:OwnedETF):
        """Let's you add an ETF in the OwnedETF"""
        pass