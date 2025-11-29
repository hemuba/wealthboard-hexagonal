from wealthboard.etf.app.ports.owned_etf_repository import OwnedETFRepository
from wealthboard.etf.domain.owned_etf import OwnedETF
from wealthboard.common.infrastructure.db.oracle_connection_provider import OracleConnectionProvider

class OracleOwnedETFRepository(OwnedETFRepository):
    
    def __init__(self, provider:OracleConnectionProvider):
        
        self._provider = provider
        
    def fetchAll(self) -> dict[str, OwnedETF]:
        conn = self._provider.get_oracledb_connection()
        cur = conn.cursor()
        cur.execute("""SELECT TICKER, NO_OF_SHARES, PURCHASE_PRICE FROM CURRENT_ETF""")
        ownedEtf: dict = {}
        for ticker, no_of_shares, p_price in cur:
            ownedEtf[ticker] =  OwnedETF(
                ticker,
                no_of_shares,
                p_price,
            )
        cur.close()
        conn.close()
        return ownedEtf
    
    def findByTicker(self, ticker: str):
        conn = self._provider.get_oracledb_connection()
        cur = conn.cursor()
        cur.execute("""SELECT TICKER, NO_OF_SHARES, PURCHASE_PRICE FROM CURRENT_ETF WHERE TICKER = :1""",
        (ticker.upper(), ))
        row= cur.fetchone()
        if row is None:
            raise ValueError(f"Ticker: {ticker.upper()} not found in your wallet")
        ticker_db, no_of_shares, purchase_price = row
        cur.close()
        conn.close()
        return OwnedETF(ticker_db, no_of_shares, purchase_price)
           
    def addEtf(self, etf:OwnedETF) -> None:
        conn = self._provider.get_oracledb_connection()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO CURRENT_ETF(TICKER, NO_OF_SHARES, PURCHASE_PRICE)
            VALUES(:1, :2, :3)""",
        (etf.ticker, etf.no_of_shares, etf.purchase_price)
        )
        conn.commit()
        cur.close()
        conn.close()
        

	
