from wealthboard.etf.app.service.owned_etf_service import OwnedETFService
from wealthboard.etf.app.use_cases.calculate_metrics import CalculateMetrics


import threading
from queue import Queue

class PortfolioMetrics:
    
    def __init__(self, owned_service: OwnedETFService, ticker_metrics: CalculateMetrics):
        self._owned_service = owned_service
        self._ticker_metrics = ticker_metrics
        
    def calculate_std_for_owned(self, date: str) -> dict[str, float]:
        etfs = self._owned_service.fetchAll()
        result_queue = Queue()
        threads = []
        
        def worker(ticker:str):
            std_dev = self._ticker_metrics.calculate_std_deviation(ticker, date)
            result_queue.put((ticker, std_dev))
            
        for etf in etfs:
            ticker= etf.ticker
            t = threading.Thread(target=worker, args=(ticker, ))
            threads.append(t)
            
            
        for t in threads:
            t.start()
            
        for t in threads:
            t.join()
            
        results = {}
        while not result_queue.empty():
            ticker, std_dev = result_queue.get()
            results[ticker] = std_dev
        return results
    
    def calculate_owned_moving_avg(self, date:str, K:int=None):
        etfs = self._owned_service.fetchAll()
        result_queue = Queue()
        threads = []
        
        def worker(ticker: str):
            moving_avg = self._ticker_metrics.calculate_moving_average(ticker, date)
            result_queue.put((ticker, moving_avg))
            
        for etf in etfs:
            ticker = etf.ticker
            t = threading.Thread(target=worker, args=(ticker, ))
            threads.append(t)
        
        for t in threads:
            t.start()
            
        for t in threads:
            t.join()
        
        results = {}
        while not result_queue.empty():
            ticker, moving_avg = result_queue.get()
            results[ticker] = moving_avg
        return results
        
            
             