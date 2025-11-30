from datetime import datetime
from decimal import Decimal

class ETFHistory:
    __slots__ = ("_data", "_ticker", "_open_price", "_close_price", "_volume")
    def __init__(self, data:datetime, ticker:str, open_price:Decimal, close_price:Decimal, volume:int):
        self._data = data
        self._ticker = ticker
        self._open_price = open_price
        self._close_price = close_price
        self._volume = volume
        
    @property
    def data(self):
        return self._data
    
    @property
    def ticker(self):
        return self._ticker
    
    @property
    def open_price(self):
        return self._open_price

    @property
    def close_price(self):
        return self._close_price
    
    @property
    def volume(self):
        return self._volume
    
    def __str__(self):
        return f"{self.data} - {self.ticker}: {self.open_price}, {self.close_price}, {self.volume}"
    
    def __repr__(self):
        return str(self)