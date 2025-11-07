from wealthboard.app.ports.etf_ports.etf_history_repository import ETFHistoryRepository
from wealthboard.domain.etf.etf_history import ETFHistory
from wealthboard.app.ports.price_provider import PriceProvider

class ETFHistoryService:
    
    def __init__(self, repo: ETFHistoryRepository, price_provider: PriceProvider):
        self._repo = repo
        self._price_provider = price_provider
        
    def fetchByTickerFromDate(self, ticker: str, date: str ) -> list[ETFHistory]:
        return sorted(list(self._repo.fetchByTickerFromDate(ticker, date).values()), key=lambda x: (x[0], x[1]))
    