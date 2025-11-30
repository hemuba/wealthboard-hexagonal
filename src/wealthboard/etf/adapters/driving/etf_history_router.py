from fastapi import APIRouter

from wealthboard.etf.app.dto.etf_history_resp_dto import ETFHistoryRespDTO
from wealthboard.etf.app.service.etf_history_service import ETFHistoryService
from wealthboard.etf.app.dto.etf_history_req_dto import ETFHistoryReqDTO
from typing import Optional

class ETFHistoryRouter:
    def __init__(self, service: ETFHistoryService):
        self._service = service
        self._router = APIRouter()


        @self._router.get("/findByTickerAndDate")
        def find_by_ticker_and_date(ticker: str, from_date: str, to_date: Optional[str] = None) -> list[
            ETFHistoryRespDTO]:
            return self._service.fetch_by_ticker_and_date(ticker, from_date, to_date)


