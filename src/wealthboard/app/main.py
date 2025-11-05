import logging
import logging.config
import os

from wealthboard.domain.ETF import ETF

logging.config.fileConfig("logging.ini")
logger = logging.getLogger(__name__)

eunl = ETF("eunl.de", "none", None, None)

print(eunl)
