# """
# ezlog.core
# A minimal wrapper for Python's built-in logging — setup in one line.
# """

# import logging
# from typing import Optional, Union


# def setup_log(
#     name: Optional[str] = None,
#     level: Union[int, str] = "INFO",
#     fmt: str = "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
#     datefmt: str = "%Y-%m-%d %H:%M:%S",
#     filename: Optional[str] = None,
# ) -> logging.Logger:
#     """
#     Create and configure a simple logger in one line.

#     Parameters
#     ----------
#     name : str, optional
#         Name of the logger. Default: root logger.
#     level : int | str, optional
#         Logging level (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
#     fmt : str, optional
#         Log format.
#     datefmt : str, optional
#         Date format.
#     filename : str, optional
#         If provided, logs will also be written to this file.

#     Returns
#     -------
#     logging.Logger
#         Configured logger instance.

#     Example
#     -------
#     >>> from ezlog import setup_log
#     >>> logger = setup_log("myapp")
#     >>> logger.info("Hello world!")
#     """
#     # Convert level to integer if given as string
#     if isinstance(level, str):
#         level = getattr(logging, level.upper(), logging.INFO)

#     # Create or get logger
#     logger = logging.getLogger(name)
#     logger.setLevel(level)

#     # Avoid duplicate handlers
#     if logger.hasHandlers():
#         logger.handlers.clear()

#     # Formatter
#     formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

#     # Console handler
#     console_handler = logging.StreamHandler()
#     console_handler.setFormatter(formatter)
#     logger.addHandler(console_handler)

#     # Optional file handler
#     if filename:
#         file_handler = logging.FileHandler(filename)
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)

#     return logger
