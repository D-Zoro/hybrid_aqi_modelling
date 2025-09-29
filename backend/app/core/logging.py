import logging
import os
import sys

from loguru import logger

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())


def configure_logging() -> None:
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    logger.configure(
        handlers=[
            {
                "sink": sys.stdout,
                "level": LOG_LEVEL,
                "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
                "enqueue": True,
            }
        ]
    )
