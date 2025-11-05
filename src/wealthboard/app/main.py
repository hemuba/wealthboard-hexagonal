import logging

import logging.config

import os

logging.config.fileConfig("logging.ini")
logger = logging.getLogger(__name__)

