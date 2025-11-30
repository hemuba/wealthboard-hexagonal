from wealthboard.common.infrastructure.db.oracle_connection_provider import OracleConnectionProvider
from wealthboard.etf.app.ports.etf_history_repository import ETFHistoryRepository
from wealthboard.etf.domain.etf_history import ETFHistory

class OracleETFHistoryRepository(ETFHistoryRepository):

    
    def __init__(self, provider: OracleConnectionProvider):
        self._provider = provider
        
    def fetch_by_ticker_and_date(self, ticker:str, from_date:str, to_date:str) -> dict[tuple, ETFHistory]:
        conn = self._provider.get_oracledb_connection()
        cur = conn.cursor()
        etf_history = {}
  
        cur.execute("""
                    SELECT DATA, TICKER, OPEN_PRICE, CLOSE_PRICE, VOLUME
                    FROM ETF_HISTORY
                    WHERE TICKER = :1
                    AND DATA >= :2
                    AND DATA <= :3
                    """, (ticker.upper(), from_date, to_date))
        for data, ticker_db, open_price, close_price, volume in cur:
            etf_history[(data, ticker_db)] = ETFHistory(
                data, 
                ticker_db, 
                open_price, 
                close_price, 
                volume)
        cur.close()
        conn.close()
        return etf_history  
        