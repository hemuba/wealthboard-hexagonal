from wealthboard.app.service.etf_services.etf_service import ETFService
from wealthboard.app.service.etf_services.owned_etf_service import OwnedETFService
from wealthboard.app.dto.etf_dto.owned_etf_dto import OwnedETFDTO
from wealthboard.app.mapper.etf_mapper.owned_etf_mapper import OwnedETFMapper
import logging


logger = logging.getLogger()

class AddOwnedETFUseCase:
    
    def __init__(self, etf_service:ETFService, owned_service:OwnedETFService):
        self._etf_service = etf_service
        self._owned_etf_service = owned_service
        
    def execute(self, dto: OwnedETFDTO):
        if not self._etf_service.exists(dto.ticker):
            logger.error(f"Ticker {dto.ticker} cannot be found, hence can't be added to your wallet.")
            return
       
        owned = OwnedETFMapper.to_entity(dto)
        self._owned_etf_service.addEtf(owned)
        logger.info(f"ETF {owned.ticker} added to your wallet.")
        
            