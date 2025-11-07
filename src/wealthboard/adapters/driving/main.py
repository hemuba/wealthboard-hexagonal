import os
from dotenv import load_dotenv

from wealthboard.adapters.driven.yfinance_price_provider import YFinancePriceProvider
from wealthboard.adapters.driven.etf_adapters.oracle_etf_repository import OracleETFRepository
from wealthboard.adapters.driven.etf_adapters.oracle_owned_etf_repository import OracleOwnedETFRepository
from wealthboard.app.service.etf_services.etf_service import ETFService
from wealthboard.app.service.etf_services.owned_etf_service import OwnedETFService
from wealthboard.infrastructure.db.connection_provider import ConnectionProvider
from wealthboard.app.use_cases.etf_use_cases.add_owned_etf import AddOwnedETFUseCase
from wealthboard.infrastructure.logging.log_config import setupLogging
from wealthboard.app.dto.etf_dto.owned_etf_dto import OwnedETFDTO
from wealthboard.adapters.driven.etf_adapters.oracle_etf_history_repository import OracleETFHistoryRepository
from wealthboard.app.service.etf_services.etf_history_service import ETFHistoryService
from wealthboard.app.use_cases.etf_use_cases.calculate_metrics import CalculateMetrics

# === BASE SETUP ===
load_dotenv()
setupLogging()

db_user = os.getenv("ORACLE_DB_USER")
db_pwd = os.getenv("ORACLE_DB_PASSWORD")
db_dsn = os.getenv("ORACLE_DB_DSN")

provider = ConnectionProvider(usr=db_user, pwd=db_pwd, dsn=db_dsn)
price_provider = YFinancePriceProvider()
# === REPO + SERVICES ===

repo_owned = OracleOwnedETFRepository(provider)
repo_etf = OracleETFRepository(provider)
repo_history = OracleETFHistoryRepository(provider)

owned_etf_service = OwnedETFService(repo_owned, price_provider)
etf_service = ETFService(repo_etf)
history_service = ETFHistoryService(repo_history, price_provider)
# === USE_CASE ===

use_case = AddOwnedETFUseCase(etf_service=etf_service, owned_service=owned_etf_service)


use_case_metrics = CalculateMetrics(historical_service=history_service, owned_sevice=owned_etf_service)

# TEST DTO
dto = OwnedETFDTO(
    ticker="CVBDW",
    no_of_shares=1,
    p_price=75.8,
)

mm_jedi = use_case_metrics.calculate_moving_average("JEDI.DE", "21-OCT-2024")

mm_test = {}
for i in range(1, len(mm_jedi)):
    if mm_jedi[i-1] < mm_jedi[i]:
        mm_test[mm_jedi[i]] = "DOWN"
    else:
        mm_test[mm_jedi[i]] = "UP"

eunl_std_dev = use_case_metrics.calculate_std_deviation(ticker="EUNL.DE", date="01-FEB-2024")

print(round(eunl_std_dev, 2))


# for k, v in all_owned.items():
#     print(k, v)

# == EXEC ==
#use_case.execute(dto)

# print(etf_service.exists("jedi.de"))



