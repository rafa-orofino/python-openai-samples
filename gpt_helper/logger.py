"""Logging utility for gpt_helper modules."""
import logging
import sys

def _build_logger(name: str = "gpt_helper", level: str | int = "INFO") -> logging.Logger:
    """Create and configure a logger with the given name and level."""
    logger = logging.getLogger(name)
    
    if logger.handlers: # avoid adding duplicate handlers
        return logger
    
    logger.setLevel(level)
    h = logging.StreamHandler(sys.stdout)
    fmt = "%(asctime)s | %(levelname)-8s | %(message)s"
    h.setFormatter(logging.Formatter(fmt, datefmt="%H:%M:%S"))
    logger.addHandler(h)
    
    return logger

logger = _build_logger()