from abc import ABC, abstractmethod

class ETFRepository(ABC):
    
    @abstractmethod
    def fetchAll(self):
        """Returns all the known ETF"""
        pass