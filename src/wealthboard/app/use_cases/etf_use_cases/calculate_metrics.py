from wealthboard.app.service.etf_services.etf_history_service import ETFHistoryService
from wealthboard.app.service.etf_services.owned_etf_service import OwnedETFService
import logging

logger = logging.getLogger()

class CalculateMetrics:
    def __init__(self, owned_sevice: OwnedETFService, historical_service: ETFHistoryService):
        self._owned_service = owned_sevice
        self._historical_service = historical_service
        
    def calculate_moving_average(self, ticker:str, date: str, K:int=None):
        windows_mmi = []
        if not K:
            K = 2
        data = sorted(
            self._historical_service.fetchByTickerFromDate(ticker, date)
            , key=lambda x: (x[0], x[1]))
        temporal_serie = [t[3] for t in data]
        for i in range(len(temporal_serie) - K + 1):
            window = temporal_serie[i:i+K]
            windows_mmi.append(sum(window) / len(window))
        return windows_mmi
        