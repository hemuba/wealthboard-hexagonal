from wealthboard.app.ports.etf_ports.owned_etf_repository import OwnedETFRepository
from wealthboard.domain.etf.owned_etf import OwnedETF
from wealthboard.infrastructure.db.connection_provider import ConnectionProvider

class OracleOwnedETFRepository(OwnedETFRepository):
    
    def __init__(self, provider:ConnectionProvider):
        
        self._provider = provider
        
    def fetchAll(self) -> dict[OwnedETF.ticker, OwnedETF]:
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
        
        