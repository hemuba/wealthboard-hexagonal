class ETF:
    
    def __init__(self, ticker, company_name, exchange, theme):
        self._ticker = ticker
        self._company_name = company_name
        self._exchange = exchange
        self._theme = theme
        
        
    @property
    def ticker(self):
        return self._ticker
    
    @property
    def company_name(self):
        return self._company_name


    @property
    def exchange(self):
        return self._exchange

    @property
    def theme(self):
        return self._theme
    
    
    def __str__(self):
        return f"{self.ticker}: {self.company_name}, {self.exchange}, {self.theme}"
    
    def __repr__(self):
        return str(self)
