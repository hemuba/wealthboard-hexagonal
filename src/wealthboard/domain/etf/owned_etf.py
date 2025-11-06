class OwnedETF:
    
    def __init__(self, ticker:str, no_of_shares:float, purchase_price:float):
        self._ticker = ticker
        self._no_of_shares = no_of_shares
        self._purchase_price = purchase_price
        self._current_price = None
        
    @property
    def ticker(self):
        return self._ticker
    
    @property
    def no_of_shares(self):
        return self._no_of_shares
    
    
    @property
    def purchase_price(self):
        return self._purchase_price
    
    @property
    def current_price(self): return self._current_price

    @current_price.setter
    def current_price(self, value: float):
        self._current_price = round(value, 2)
    
    @property
    def current_return(self):
        return round((self.current_price / self.purchase_price - 1) * 100, 2)
    
    @property
    def current_total(self):
        return round(self.current_return * self.no_of_shares, 2)
    
    def __str__(self):
        return f"{self.ticker}: {self.no_of_shares}, {self.purchase_price}, {self.current_price}, {self.current_return}, {self.current_total}"
    
    
    def __repr__(self):
        return str(self)