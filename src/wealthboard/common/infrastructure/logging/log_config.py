import logging
import logging.config
import sys

def setupLogging():
    path = "logging.ini"
    logging.config.fileConfig(path, disable_existing_loggers=False, defaults={"sys": sys})