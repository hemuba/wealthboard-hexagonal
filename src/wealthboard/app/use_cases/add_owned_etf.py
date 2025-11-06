from wealthboard.app.service.etf_service import ETFService
from wealthboard.app.service.owned_etf_service import OwnedETFService
from wealthboard.domain.owned_etf import OwnedETF

class AddOwnedETFUseCase:
    
    def __init__(self, etf_service:ETFService, owned_service:OwnedETFService):
        self._etf_service = etf_service
        self._owned_etf_service = owned_service
        
    def execute(self, etf: OwnedETF):
        
        if self._etf_service.exists(etf.ticker):
            self._owned_etf_service.addEtf(etf)
            print(f"ETF {etf.ticker} added to your wallet.")
        else:
            raise ValueError(f"Ticker {etf.ticker} cannot be found, hence can't be added to your wallet.")
            