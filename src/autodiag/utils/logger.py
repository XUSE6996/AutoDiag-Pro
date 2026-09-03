import logging


def create_logger():

    logger = logging.getLogger(
        "AutoDiag"
    )

    logger.setLevel(
        logging.INFO
    )

    return logger
