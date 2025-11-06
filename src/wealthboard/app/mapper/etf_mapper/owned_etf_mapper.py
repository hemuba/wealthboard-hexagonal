from wealthboard.app.dto.etf_dto.owned_etf_dto import OwnedETFDTO
from wealthboard.domain.etf.owned_etf import OwnedETF

class OwnedETFMapper:
    
    @staticmethod
    def to_entity(dto: OwnedETFDTO) -> OwnedETF:
        """Converts a DTO to an Owned ETF entity"""
        return OwnedETF(
            ticker=dto.ticker.upper(),
            no_of_shares=dto.no_of_shares,
            purchase_price=dto.p_price
        )
    
    @staticmethod
    def to_dto(owned_etf: OwnedETF) -> OwnedETFDTO:
        """Converts an Owned ETF Entity to a DTO"""
        return OwnedETFDTO(
            ticker=owned_etf.ticker.upper(),
            no_of_shares=owned_etf.no_of_shares,
            p_price=owned_etf.purchase_price
        )