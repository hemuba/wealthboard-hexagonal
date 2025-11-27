from wealthboard.common.infrastructure.db.oracle_connection_provider import OracleConnectionProvider
from wealthboard.etf.app.ports.etf_history_repository import ETFHistoryRepository
from wealthboard.etf.domain.etf_history import ETFHistory

class OracleETFHistoryRepository(ETFHistoryRepository):

    
    def __init__(self, provider: OracleConnectionProvider):
        self._provider = provider
        
    def fetchByTickerFromDate(self, tickers:str, from_date:str) -> dict[tuple, ETFHistory]:
        conn = self._provider.get_oracledb_connection()
        cur = conn.cursor()
        etf_history = {}
        
        ticker_list = [t.strip().upper() for t in tickers.split(",")]
        placeholders = ",".join([f":{i+1}" for i in range(len(ticker_list))])
        cur.execute(f"""
                    SELECT DATA, TICKER, OPEN_PRICE, CLOSE_PRICE, VOLUME
                    FROM ETF_HISTORY
                    WHERE TICKER IN ({placeholders}) AND DATA >= :{len(ticker_list) + 1} 
                    """, tuple(ticker_list) + (from_date, ))
        for data, ticker, open_price, close_price, volume in cur:
            etf_history[(data, ticker)] = data, ticker, open_price, close_price, volume
        cur.close()
        conn.close()
        return etf_history  
        