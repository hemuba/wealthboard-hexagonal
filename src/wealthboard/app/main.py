import logging
import logging.config
import os
from dotenv import load_dotenv



from wealthboard.domain.ETF import ETF
from wealthboard.domain.OwnedETF import OwnedETF
from wealthboard.driven.adapters.OracleETFRepository import OracleETFRepository
from wealthboard.driven.adapters.OracleOwnedETFRepository import OracleOwnedETFRepository
from wealthboard.app.ETFService import ETFService
from wealthboard.app.OwnedETFService import OwnedETFService

load_dotenv()
db_user = os.getenv("ORACLE_DB_USER")
db_pwd = os.getenv("ORACLE_DB_PASSWORD")
db_dsn = os.getenv("ORACLE_DB_DSN")


logging.config.fileConfig("logging.ini")
logger = logging.getLogger(__name__)



repo = OracleETFRepository(usr=db_user, pwd=db_pwd, dsn=db_dsn)
repo_owned = OracleOwnedETFRepository(usr=db_user, pwd=db_pwd, dsn=db_dsn)
etf_service = ETFService(repo)
owned_etf_service = OwnedETFService(repo_owned)

eunl = etf_service.findByTicker("jedi.DE")
all_owned = owned_etf_service.fetchAll()
#all = use_case.fetchAll()

for t in all_owned:
    print(t)

