from wealthboard.driven.ports.ETFRepository import ETFRepository
import oracledb as odb
from wealthboard.domain.ETF import ETF

class OracleETFRepository(ETFRepository):
    
    def __init__(self, usr: str, pwd: str, dsn: str):
        self._usr = usr
        self._pwd = pwd
        self._dsn = dsn

    
    def fetchAll(self):
        
        conn = odb.connect(user=self._usr, password=self._pwd, dsn=self._dsn)
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
        
        
        