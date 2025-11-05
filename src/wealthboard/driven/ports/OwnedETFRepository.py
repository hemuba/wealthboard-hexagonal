from abc import ABC, abstractmethod

class OwnedETFRepository(ABC):
    
    @abstractmethod
    def fetchAll(self):
        """Returns all the Owned ETF"""
    pass