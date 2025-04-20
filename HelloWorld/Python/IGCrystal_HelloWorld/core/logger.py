"""日志系统，提供应用日志记录功能喵～"""

import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from typing import Any, Dict, Optional


class LoggerFactory:
    """日志工厂类，创建和管理日志器喵～"""

    _loggers: Dict[str, logging.Logger] = {}

    @classmethod
    def get_logger(cls, name: str = "main", log_level: str = "INFO") -> logging.Logger:
        """获取或创建一个日志器喵～

        Args:
            name: 日志器名称
            log_level: 日志级别

        Returns:
            日志器实例
        """
        if name in cls._loggers:
            return cls._loggers[name]

        # 创建新的日志器
        logger = logging.getLogger(name)

        # 设置日志级别
        level = getattr(logging, log_level.upper(), logging.INFO)
        logger.setLevel(level)

        # 防止日志消息传递到父级logger
        logger.propagate = False

        # 添加控制台处理器
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # 添加文件处理器
        logs_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs"
        )
        os.makedirs(logs_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            os.path.join(logs_dir, f"{name}.log"),
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding="utf-8",
        )
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # 存储日志器
        cls._loggers[name] = logger
        return logger


class Logger:
    """日志包装器，提供便捷的日志方法喵～"""

    def __init__(self, name: str = "main", log_level: str = "INFO") -> None:
        """初始化日志器喵～

        Args:
            name: 日志器名称
            log_level: 日志级别
        """
        self.logger = LoggerFactory.get_logger(name, log_level)

    def debug(self, message: str, *args: Any, **kwargs: Any) -> None:
        """记录调试信息喵～

        Args:
            message: 日志消息
            *args: 位置参数
            **kwargs: 关键字参数
        """
        self.logger.debug(message, *args, **kwargs)

    def info(self, message: str, *args: Any, **kwargs: Any) -> None:
        """记录一般信息喵～

        Args:
            message: 日志消息
            *args: 位置参数
            **kwargs: 关键字参数
        """
        self.logger.info(message, *args, **kwargs)

    def warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        """记录警告信息喵～

        Args:
            message: 日志消息
            *args: 位置参数
            **kwargs: 关键字参数
        """
        self.logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args: Any, **kwargs: Any) -> None:
        """记录错误信息喵～

        Args:
            message: 日志消息
            *args: 位置参数
            **kwargs: 关键字参数
        """
        self.logger.error(message, *args, **kwargs)

    def critical(self, message: str, *args: Any, **kwargs: Any) -> None:
        """记录严重错误信息喵～

        Args:
            message: 日志消息
            *args: 位置参数
            **kwargs: 关键字参数
        """
        self.logger.critical(message, *args, **kwargs)

    def exception(self, message: str, *args: Any, **kwargs: Any) -> None:
        """记录异常信息喵～

        Args:
            message: 日志消息
            *args: 位置参数
            **kwargs: 关键字参数
        """
        self.logger.exception(message, *args, **kwargs)
