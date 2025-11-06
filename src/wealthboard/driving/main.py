import os
from dotenv import load_dotenv
from logging import getLogger


from wealthboard.domain.etf import ETF
from wealthboard.domain.owned_etf import OwnedETF
from wealthboard.driven.adapters.oracle_etf_repository import OracleETFRepository
from wealthboard.driven.adapters.oracle_owned_etf_repository import OracleOwnedETFRepository
from wealthboard.app.service.etf_service import ETFService
from wealthboard.app.service.owned_etf_service import OwnedETFService
from wealthboard.infrastructure.db.connection_provider import ConnectionProvider
from wealthboard.app.use_cases.add_owned_etf import AddOwnedETFUseCase
from wealthboard.infrastructure.logging.log_config import setupLogging

load_dotenv()
setupLogging()

db_user = os.getenv("ORACLE_DB_USER")
db_pwd = os.getenv("ORACLE_DB_PASSWORD")
db_dsn = os.getenv("ORACLE_DB_DSN")

logger = getLogger(__name__)

provider = ConnectionProvider(usr=db_user, pwd=db_pwd, dsn=db_dsn)


repo_owned = OracleOwnedETFRepository(provider)
repo_etf = OracleETFRepository(provider)

owned_etf_service = OwnedETFService(repo_owned)
etf_service = ETFService(repo_etf)

use_case = AddOwnedETFUseCase(etf_service=etf_service, owned_service=owned_etf_service)

print(etf_service.exists("jedi.de"))
logger.info("EEE")


