from wealthboard.driven.ports.OwnedETFRepository import OwnedETFRepository
from wealthboard.domain.OwnedETF import OwnedETF
import oracledb as odb

class OracleOwnedETFRepository(OwnedETFRepository):
    
    def __init__(self, usr:str, pwd:str, dsn:str):
        
        self._usr = usr
        self._pwd = pwd
        self._dsn = dsn
        
    def fetchAll(self) -> dict[OwnedETF.ticker, OwnedETF]:
        
        conn = odb.connect(user=self._usr, password=self._pwd, dsn=self._dsn)
        cur = conn.cursor()
        cur.execute("""SELECT TICKER, NO_OF_SHARES, PURCHASE_PRICE, CURRENT_PRICE FROM CURRENT_ETF""")
        ownedEtf: dict = {}
        for ticker, no_of_shares, p_price, c_price in cur:
            ownedEtf[ticker] =  OwnedETF(
                ticker,
                no_of_shares,
                p_price,
                c_price
            )
        cur.close()
        conn.close()
        return ownedEtf
        