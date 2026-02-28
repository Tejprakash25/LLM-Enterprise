"""Loguru-based logging setup."""
import sys
from pathlib import Path
from loguru import logger
from backend.core.config import settings


def setup_logging() -> None:
    Path("logs").mkdir(exist_ok=True)
    logger.remove()
    logger.add(sys.stdout, level=settings.LOG_LEVEL, colorize=True)
    logger.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="1 day",
        retention="7 days",
        level=settings.LOG_LEVEL,
    )
