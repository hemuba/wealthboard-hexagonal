from wealthboard.etf.app.ports.owned_etf_repository import OwnedETFRepository
from wealthboard.etf.domain.owned_etf import OwnedETF
from wealthboard.common.app.ports.price_provider import PriceProvider
from wealthboard.etf.app.dto.resp_owned_dto import RespOwnedDTO 
from wealthboard.etf.app.mapper.owned_etf_mapper import OwnedETFMapper
from wealthboard.etf.app.dto.req_owned_dto import ReqOwnedDTO
from decimal import Decimal

class OwnedETFService:

    def __init__(self, repo: OwnedETFRepository, price_provider: PriceProvider):
        
        self._repo = repo
        self._price_provider = price_provider
        
    def fetchAll(self) -> list[RespOwnedDTO]:
        etfs = list(self._repo.fetchAll().values())
        for e in etfs:
          e.current_price = self._price_provider.get_current_price(e.ticker)
        return [OwnedETFMapper.to_dto(e) for e in etfs]

    def findByTicker(self, ticker: str) -> RespOwnedDTO:
        etf = self._repo.findByTicker(ticker)
        etf.current_price = self._price_provider.get_current_price(etf.ticker)
        return OwnedETFMapper.to_dto(etf)
            
        
    def addEtf(self, dto: ReqOwnedDTO):
        entity = OwnedETFMapper.to_entity(dto)
        self._repo.addEtf(entity)
        
    def getPrice(self) -> dict[str, Decimal]:
        current_prices = {}
        for t in self.fetchAll():
            current_prices[t.ticker] = t.current_price
        return current_prices

    
    def get_percentage_return(self) -> dict[str, Decimal]:
        current_percentage_return = {}
        for t in self.fetchAll():
            current_percentage_return[t.ticker] = t.current_return 
        return dict(sorted(current_percentage_return.items(), key=lambda x: x[1], reverse=True))