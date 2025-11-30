from decimal import Decimal

from wealthboard.etf.app.dto.resp_owned_dto import RespOwnedDTO
from wealthboard.etf.app.service.owned_etf_service import OwnedETFService
from fastapi import APIRouter
class OwnedETFRouter:
    def __init__(self, etf_service: OwnedETFService):
        self._service = etf_service
        self._router = APIRouter()

        @self._router.get("/fetchAll")
        def fetch_all() -> list[RespOwnedDTO]:
            return self._service.fetch_all()

        @self._router.get("/getPrices")
        def get_prices() -> dict[str, Decimal]:
            return self._service.get_price()

        @self._router.get("/getPercentageReturn")
        def get_percentage_return() -> dict[str, Decimal]:
            return self._service.get_percentage_return()

