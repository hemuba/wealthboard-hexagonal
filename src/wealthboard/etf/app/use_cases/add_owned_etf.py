from wealthboard.etf.app.service.etf_service import ETFService
from wealthboard.etf.app.service.owned_etf_service import OwnedETFService
from wealthboard.etf.app.dto.req_owned_dto import ReqOwnedDTO
from wealthboard.etf.app.mapper.owned_etf_mapper import OwnedETFMapper
import logging


logger = logging.getLogger()

class AddOwnedETFUseCase:
    
    def __init__(self, etf_service:ETFService, owned_service:OwnedETFService):
        self._etf_service = etf_service
        self._owned_etf_service = owned_service
        
    def execute(self, dto: ReqOwnedDTO):
        if not self._etf_service.exists(dto.ticker):
            logger.error(f"Ticker {dto.ticker} cannot be found, hence can't be added to your wallet.")
            return
       
        owned = OwnedETFMapper.to_entity(dto)
        self._owned_etf_service.addEtf(owned)
        logger.info(f"ETF {owned.ticker} added to your wallet.")
        
            