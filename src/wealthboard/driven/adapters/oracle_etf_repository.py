from wealthboard.driven.ports.etf_repository import ETFRepository
import oracledb as odb
from wealthboard.domain.etf import ETF
from wealthboard.infrastructure.db.connection_provider import ConnectionProvider

class OracleETFRepository(ETFRepository):
    
    def __init__(self, provider = ConnectionProvider):
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
 
        