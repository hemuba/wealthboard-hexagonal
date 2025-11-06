import os
from dotenv import load_dotenv
from logging import getLogger

from wealthboard.driven.adapters.yfinance_price_provider import YFinancePriceProvider
from wealthboard.driven.adapters.oracle_etf_repository import OracleETFRepository
from wealthboard.driven.adapters.oracle_owned_etf_repository import OracleOwnedETFRepository
from wealthboard.app.service.etf_service import ETFService
from wealthboard.app.service.owned_etf_service import OwnedETFService
from wealthboard.infrastructure.db.connection_provider import ConnectionProvider
from wealthboard.app.use_cases.add_owned_etf import AddOwnedETFUseCase
from wealthboard.infrastructure.logging.log_config import setupLogging
from wealthboard.app.dto.owned_etf_dto import OwnedETFDTO


# === BASE SETUP ===
load_dotenv()
setupLogging()
logger = getLogger(__name__)

db_user = os.getenv("ORACLE_DB_USER")
db_pwd = os.getenv("ORACLE_DB_PASSWORD")
db_dsn = os.getenv("ORACLE_DB_DSN")

provider = ConnectionProvider(usr=db_user, pwd=db_pwd, dsn=db_dsn)
price_provider = YFinancePriceProvider()
# === REPO + SERVICES ===

repo_owned = OracleOwnedETFRepository(provider)
repo_etf = OracleETFRepository(provider)

owned_etf_service = OwnedETFService(repo_owned, price_provider)
etf_service = ETFService(repo_etf)
# === USE_CASE ===

use_case = AddOwnedETFUseCase(etf_service=etf_service, owned_service=owned_etf_service)

# TEST DTO
dto = OwnedETFDTO(
    ticker="CVBDW",
    no_of_shares=1,
    p_price=75.8,
    c_price=80.2
)

all_owned = owned_etf_service.fetchAll()

for t in all_owned:
    print(t)

# == EXEC ==
#use_case.execute(dto)

# print(etf_service.exists("jedi.de"))



