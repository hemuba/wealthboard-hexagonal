from wealthboard.etf.app.dto.req_owned_dto import ReqOwnedDTO
from wealthboard.etf.domain.owned_etf import OwnedETF
from wealthboard.etf.app.dto.resp_owned_dto import RespOwnedDTO


class OwnedETFMapper:
    
    @staticmethod
    def to_entity(dto: ReqOwnedDTO) -> OwnedETF:
        """Converts a DTO to an Owned ETF entity"""
        return OwnedETF(
            ticker=dto.ticker.upper(),
            no_of_shares=dto.no_of_shares,
            purchase_price=dto.purchase_price
        )
    
    @staticmethod
    def to_dto(owned_etf: OwnedETF) -> RespOwnedDTO:
        return RespOwnedDTO(
            ticker=owned_etf.ticker.upper(),
            no_of_shares= owned_etf.no_of_shares,
            purchase_price= owned_etf.purchase_price,
            current_price= owned_etf.current_price,
            current_return= owned_etf.current_return,
            current_total= owned_etf.current_total
        )
