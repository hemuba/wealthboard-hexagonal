from wealthboard.etf.app.service.owned_etf_service import OwnedETFService
from wealthboard.etf.app.use_cases.calculate_metrics import CalculateMetrics
from wealthboard.etf.app.service.etf_history_service import ETFHistoryService


import threading
from queue import Queue

class MultipleMetrics:
    
    def __init__(self, owned_service: OwnedETFService, ticker_metrics: CalculateMetrics, history_service: ETFHistoryService):
        self._owned_service = owned_service
        self._ticker_metrics = ticker_metrics
        self._history_service = history_service
        
    def calculate_std_for_owned(self, from_date: str, to_date:str=None) -> dict[str, float]:
        etfs = self._owned_service.fetch_all()
        result_queue = Queue()
        threads = []
        
        def worker(ticker:str):
            std_dev = self._ticker_metrics.calculate_std_deviation(ticker, from_date, to_date)
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
    
    def calculate_owned_moving_avg(self, from_date:str, to_date:str=None, K:int=None):
        etfs = self._owned_service.fetch_all()
        result_queue = Queue()
        threads = []
        
        def worker(ticker: str):
            moving_avg = self._ticker_metrics.calculate_moving_average(ticker, from_date, to_date, K)
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
    
    def calculate_multiple_pct_returns(self, tickers:list[str], from_date: str, to_date:str=None):
        result_queue = Queue()
        threads = []
        
        def worker(ticker: str):
            pct_returns = self._ticker_metrics.calculate_percentage_return(ticker, from_date, to_date)
            result_queue.put((ticker, pct_returns))

        for ticker in tickers:
            t = threading.Thread(target=worker, args=(ticker, ))
            threads.append(t)
            
        for t in threads:
            t.start()
            
        for t in threads:
            t.join()
        
        results = {}
        while not result_queue.empty():
            ticker, pct_ret = result_queue.get()
            results[ticker] = pct_ret
        return results
            
             