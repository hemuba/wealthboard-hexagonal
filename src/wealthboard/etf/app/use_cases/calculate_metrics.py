from wealthboard.etf.app.service.etf_history_service import ETFHistoryService
from wealthboard.etf.app.service.owned_etf_service import OwnedETFService

class CalculateMetrics:
    def __init__(self, owned_sevice: OwnedETFService, historical_service: ETFHistoryService):
        self._owned_service = owned_sevice
        self._historical_service = historical_service
  
    def calculate_moving_average(self, ticker:str, date: str, K:int=None) -> list[float]:
        temporal_serie = self._historical_service.get_temporal_serie(ticker, date)
        windows_mmi = []
        if not K:
            K = 2
        for i in range(len(temporal_serie) - K + 1):
            window = temporal_serie[i:i+K]
            windows_mmi.append(sum(window) / len(window))
        return windows_mmi
        
    
    def calculate_std_deviation(self, ticker:str, date: str) -> float:
        data = self._historical_service.calculate_percentage_return(ticker, date)
        if len(data) < 2:
            return 0.0
        ma = sum(data) / len(data)
        sq_deviation_sum = 0
        for i in range(len(data)):
            sq_deviation_sum += (data[i] - ma) ** 2
        variance = sq_deviation_sum / (len(data) - 1)
        std_dev = (variance ** 0.5) * 100
        return round(std_dev, 2)