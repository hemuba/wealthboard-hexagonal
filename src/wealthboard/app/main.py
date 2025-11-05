import logging
import logging.config
import os
from dotenv import load_dotenv



from wealthboard.domain.ETF import ETF
from wealthboard.domain.OwnedETF import OwnedETF
from wealthboard.driven.adapters.OracleETFRepository import OracleETFRepository
from wealthboard.app.ETFService import ETFService


load_dotenv()
db_user = os.getenv("ORACLE_DB_USER")
db_pwd = os.getenv("ORACLE_DB_PASSWORD")
db_dsn = os.getenv("ORACLE_DB_DSN")


logging.config.fileConfig("logging.ini")
logger = logging.getLogger(__name__)



repo = OracleETFRepository(usr=db_user, pwd=db_pwd, dsn=db_dsn)
service = ETFService(repo)

for k, v in service.fetchAll().items():
    if k == "EUNL.DE":
        print(k, v)
