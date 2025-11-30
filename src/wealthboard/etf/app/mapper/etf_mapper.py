from wealthboard.etf.app.dto.req_owned_dto import ReqOwnedDTO
from wealthboard.etf.domain.owned_etf import OwnedETF
from wealthboard.etf.app.dto.resp_owned_dto import RespOwnedDTO
from wealthboard.etf.app.dto.etf_dto import ETFDTO
from wealthboard.etf.app.dto.etf_history_req_dto import ETFHistoryReqDTO
from wealthboard.etf.app.dto.etf_history_resp_dto import ETFHistoryRespDTO
from wealthboard.etf.domain.etf import ETF
from wealthboard.etf.domain.etf_history import ETFHistory
from decimal import Decimal


class ETFMapper:
    
    @staticmethod
    def etf_to_entity(dto: ETFDTO) -> ETF:
        return ETF(
            ticker=dto.ticker.upper(),
            company_name=dto.company_name.capitalize(),
            exchange=dto.exchange.upper(),
            theme=dto.theme
        )
        
    @staticmethod
    def etf_to_dto(entity: ETF) -> ETFDTO:
        return ETFDTO(
            ticker=entity.ticker,
            company_name=entity.company_name,
            exchange=entity.exchange,
            theme=entity.theme
        )
    
    @staticmethod
    def history_to_entity(dto: ETFHistoryReqDTO) -> ETFHistory:
        return ETFHistory(
            data=dto.data,
            ticker=dto.ticker.upper(),
            open_price=Decimal(str(dto.open_price)),
            close_price=Decimal(str(dto.close_price)),
            volume=int(dto.volume),
        )

    @staticmethod
    def history_to_dto(entity: ETFHistory) -> ETFHistoryRespDTO:
        return ETFHistoryRespDTO(
            data=entity.data,
            ticker=entity.ticker,
            open_price=float(entity.open_price),
            close_price=float(entity.close_price),
            volume=entity.volume
        )
    
    @staticmethod
    def owned_to_entity(dto: ReqOwnedDTO) -> OwnedETF:
        return OwnedETF(
            ticker=dto.ticker.upper(),
            no_of_shares=dto.no_of_shares,
            purchase_price=dto.purchase_price
        )
    
    @staticmethod
    def owned_to_dto(owned_etf: OwnedETF) -> RespOwnedDTO:
        return RespOwnedDTO(
            ticker=owned_etf.ticker.upper(),
            no_of_shares= owned_etf.no_of_shares,
            purchase_price= owned_etf.purchase_price,
            current_price= owned_etf.current_price,
            current_return= owned_etf.current_return,
            current_total= owned_etf.current_total
        )
