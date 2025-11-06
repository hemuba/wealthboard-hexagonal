from datetime import datetime
class ETFHistory:
    
    def __init__(self, data:datetime, ticker:str, open_price:float, close_price:float, volume:float):
        self._data = data
        self._ticker = ticker
        self._open_price = open_price
        self._close_price = close_price
        self._volume = volume
        self._current_price = None
        
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
        return f"{self.data} - {self.ticker}: {self.open_price}, {self.close_price}, {self.volume}, {self._current_price}"
    
    def __repr__(self):
        return str(self)