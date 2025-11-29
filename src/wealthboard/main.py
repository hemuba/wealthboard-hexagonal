import os
from dotenv import load_dotenv

from wealthboard.common.adapters.driven.yfinance_price_provider import YFinancePriceProvider
from wealthboard.etf.adapters.driven.oracle_etf_repository import OracleETFRepository
from wealthboard.etf.adapters.driven.oracle_owned_etf_repository import OracleOwnedETFRepository
from wealthboard.etf.app.service.owned_etf_service import OwnedETFService
from wealthboard.etf.app.service.etf_service import ETFService
from wealthboard.common.infrastructure.db.oracle_connection_provider import OracleConnectionProvider
from wealthboard.etf.app.use_cases.add_owned_etf import AddOwnedETFUseCase
from wealthboard.common.infrastructure.logging.log_config import setupLogging
from wealthboard.etf.app.dto.req_owned_dto import ReqOwnedDTO
from wealthboard.etf.adapters.driven.oracle_etf_history_repository import OracleETFHistoryRepository
from wealthboard.etf.app.service.etf_history_service import ETFHistoryService
from wealthboard.etf.app.use_cases.calculate_metrics import CalculateMetrics
from wealthboard.etf.adapters.decorators.cache_owned_etf_repository import CacheOwnedETFRepository
from wealthboard.etf.app.use_cases.multiple_metrics import MultipleMetrics

# === BASE SETUP ===
load_dotenv()
setupLogging()

db_user = os.getenv("ORACLE_DB_USER")
db_pwd = os.getenv("ORACLE_DB_PASSWORD")
db_dsn = os.getenv("ORACLE_DB_DSN")

provider = OracleConnectionProvider(usr=db_user, pwd=db_pwd, dsn=db_dsn)
price_provider = YFinancePriceProvider()
# === REPO ===

repo_owned = OracleOwnedETFRepository(provider)
repo_etf = OracleETFRepository(provider)
repo_history = OracleETFHistoryRepository(provider)


# === CACHE ===
owned_etf_cache = CacheOwnedETFRepository(repo_owned)

# === SERVICES === 
owned_etf_service = OwnedETFService(owned_etf_cache, price_provider)
etf_service = ETFService(repo_etf)
history_service = ETFHistoryService(repo_history, price_provider)

# === USE_CASE ===
use_case_add_owned = AddOwnedETFUseCase(etf_service=etf_service, owned_service=owned_etf_service)
use_case_metrics = CalculateMetrics(historical_service=history_service, owned_service=owned_etf_service)
use_case_portfolio = MultipleMetrics(owned_etf_service, use_case_metrics, history_service)

to_use = use_case_portfolio.calculate_std_for_owned("01-JAN-2024")
to_use_2 = use_case_portfolio.calculate_owned_moving_avg("01-AUG-2025")
to_use_3 = use_case_portfolio.calculate_multiple_pct_returns(["EUNL.DE", "IS3N.DE"], "01-JAN-20")


for t in owned_etf_service.fetchAll():
    print(t)
# for k, v in all_owned.items():
#     print(k, v)

# == EXEC ==
#use_case.execute(dto)

# print(etf_service.exists("jedi.de"))



