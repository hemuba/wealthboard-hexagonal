from wealthboard.etf.app.ports.etf_repository import ETFRepository
from wealthboard.etf.domain.etf import ETF
from wealthboard.common.infrastructure.db.oracle_connection_provider import OracleConnectionProvider

class OracleETFRepository(ETFRepository):
    
    def __init__(self, provider = OracleConnectionProvider):
        self._provider = provider

    
    def fetchAll(self):
        
        conn = self._provider.get_oracledb_connection()
        cur = conn.cursor()
        cur.execute("""SELECT TICKER, COMPANY_NAME, EXCHANGE, THEME FROM ETF""")
        etf: dict = {}
        for ticker, company_name, exchange, theme in cur:
              etf[ticker] = ETF(
                  ticker, 
                  company_name,
                  exchange,
                  theme
              )
        cur.close()
        conn.close()
        return etf
 
        