from decimal import Decimal, ROUND_HALF_UP

class OwnedETF:
    __slots__ = ("_ticker", "_no_of_shares", "_purchase_price", "_current_price")
    def __init__(self, ticker:str, no_of_shares:Decimal, purchase_price:Decimal):
        self._ticker = ticker
        self._no_of_shares = Decimal(str(no_of_shares))
        self._purchase_price = Decimal(str(purchase_price))
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
        dec = Decimal(str(value))
        self._current_price = dec.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    @property
    def current_return(self):
        if self.current_price is None:
            return None
        res = (self.current_price / self.purchase_price - Decimal("1")) * Decimal("100");
        return res.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    @property
    def current_total(self):
        if self.current_price is None:
            return None
        res = self._no_of_shares * self.current_price
        return res.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            
    def __str__(self):
        return f"{self.ticker}: {self.no_of_shares}, {self.purchase_price}, {self.current_price}, {self.current_return}, {self.current_total}"
    
    
    def __repr__(self):
        return str(self)