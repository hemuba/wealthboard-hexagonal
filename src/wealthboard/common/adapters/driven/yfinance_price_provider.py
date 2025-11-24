import yfinance as yf
import logging

from wealthboard.common.app.ports.price_provider import PriceProvider
    
    
class YFinancePriceProvider(PriceProvider):
    
        
    def __init__(self):
        logging.getLogger("yfinance").setLevel(logging.WARNING)
        logging.getLogger("peewee").setLevel(logging.WARNING)
    
    def get_current_price(self, ticker:str) -> float:
        ticker_obj = yf.Ticker(ticker)
        return float(ticker_obj.fast_info["last_price"])
        