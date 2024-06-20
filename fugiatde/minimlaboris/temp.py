import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
    # Code that may raise an error
    pass
except Exception as e:
    logger.error("An error occurred: %s", str(e))
