# gpt_helper/logger.py
import logging
import sys

def _build_logger(name: str = "gpt_helper", level: str | int = "INFO") -> logging.Logger:
    """Cria e configura um logger com o nome e nível especificados."""
    logger = logging.getLogger(name)
    
    if logger.handlers: # evita adicionar duplicado
        return logger
    
    logger.setLevel(level)
    h = logging.StreamHandler(sys.stdout)
    fmt = "%(asctime)s | %(levelname)-8s | %(message)s"
    h.setFormatter(logging.Formatter(fmt, datefmt="%H:%M:%S"))
    logger.addHandler(h)
    
    return logger

logger = _build_logger()