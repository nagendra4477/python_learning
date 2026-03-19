import logging
logger = logging.getLogger(__name__)


def extract_data():
    logger.info("Starting data extraction")
    return ["row1", "row2", "row3"]

print(extract_data())