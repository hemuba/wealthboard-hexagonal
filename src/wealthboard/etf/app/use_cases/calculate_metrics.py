from wealthboard.etf.app.service.etf_history_service import ETFHistoryService
from wealthboard.etf.app.service.owned_etf_service import OwnedETFService
from datetime import datetime

class CalculateMetrics:
    def __init__(self, owned_sevice: OwnedETFService, historical_service: ETFHistoryService):
        self._owned_service = owned_sevice
        self._historical_service = historical_service
        
    def calculate_percentage_return(self, ticker:str, from_date: str, to_date:str=None) -> list[float]:
        pct_returns = [] 
        temporal_serie = self._historical_service.get_temporal_serie(ticker, from_date, to_date) 
        for i in range(1, len(temporal_serie)): 
            pct_returns.append(temporal_serie[i] / temporal_serie[i-1] - 1) 
        return pct_returns
  
    def calculate_moving_average(self, ticker:str, from_date: str, to_date:str=None, K:int=None) -> list[float]:
        temporal_serie = self._historical_service.get_temporal_serie(ticker, from_date, to_date)
        windows_mmi = []
        if not K:
            K = 2
        for i in range(len(temporal_serie) - K + 1):
            window = temporal_serie[i:i+K]
            windows_mmi.append(sum(window) / len(window))
        return windows_mmi
        
    
    def calculate_std_deviation(self, ticker:str, from_date:str, to_date:str=None) -> float:
      
        data = self.calculate_percentage_return(ticker, from_date, to_date)
        if len(data) < 2:
            return 0.0
        ma = sum(data) / len(data)
        sq_deviation_sum = 0
        for i in range(len(data)):
            sq_deviation_sum += (data[i] - ma) ** 2
        variance = sq_deviation_sum / (len(data) - 1)
        std_dev = (variance ** 0.5) * 100
        return round(std_dev, 2)
    
    
    