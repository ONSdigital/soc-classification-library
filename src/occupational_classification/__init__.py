__version__ = "0.0.1"

from ._config.main import check_file_exists, get_config
from .logs import setup_logging

__all__ = ["check_file_exists", "get_config", "setup_logging"]
