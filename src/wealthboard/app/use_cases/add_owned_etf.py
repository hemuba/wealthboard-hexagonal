from wealthboard.app.service.etf_service import ETFService
from wealthboard.app.service.owned_etf_service import OwnedETFService
from wealthboard.domain.owned_etf import OwnedETF
from wealthboard.app.dto.owned_etf_dto import OwnedETFDTO
from wealthboard.infrastructure.logging.log_config import setupLogging
from wealthboard.app.mapper.owned_etf_mapper import OwendETFMapper
import logging

setupLogging()
logger = logging.getLogger()

class AddOwnedETFUseCase:
    
    def __init__(self, etf_service:ETFService, owned_service:OwnedETFService):
        self._etf_service = etf_service
        self._owned_etf_service = owned_service
        
    def execute(self, dto: OwnedETFDTO):
        if not self._etf_service.exists(dto.ticker):
            logger.error(f"Ticker {dto.ticker} cannot be found, hence can't be added to your wallet.")
            return
       
        owned = OwendETFMapper.to_entity(dto)
        self._owned_etf_service.addEtf(owned)
        logger.info(f"ETF {owned.ticker} added to your wallet.")
        
            