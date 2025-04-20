"""异常处理模块，提供全局异常捕获和处理功能喵～"""

import sys
import traceback
from types import TracebackType  # 从types模块导入TracebackType喵～
from typing import Any, Callable, Dict, List, Optional, Type


class ExceptionHandler:
    """异常处理器，管理应用中的异常喵～"""

    def __init__(self, logger: Any) -> None:
        """初始化异常处理器喵～

        Args:
            logger: 日志记录器
        """
        self.logger = logger
        self.handlers: Dict[Type[Exception], Callable] = {}

        # 注册默认处理器
        self.register_handler(Exception, self._default_handler)

    def register_handler(
        self, exception_type: Type[Exception], handler: Callable
    ) -> None:
        """注册异常处理函数喵～

        Args:
            exception_type: 要处理的异常类型
            handler: 处理函数
        """
        self.handlers[exception_type] = handler

    def handle(self, exc: Exception) -> bool:
        """处理异常，返回是否成功处理喵～

        Args:
            exc: 要处理的异常

        Returns:
            是否成功处理异常
        """
        # 查找最匹配的异常处理器
        handler = None
        for exc_type, h in self.handlers.items():
            if isinstance(exc, exc_type):
                handler = h
                break

        # 如果没有找到处理器，使用默认处理器
        if handler is None:
            handler = self._default_handler

        # 执行处理器
        try:
            handler(exc)
            return True
        except Exception as handler_exc:
            self.logger.error(f"异常处理器发生错误: {str(handler_exc)}")
            self._default_handler(exc)
            return False

    def _default_handler(self, exc: Exception) -> None:
        """默认异常处理函数喵～

        Args:
            exc: 要处理的异常
        """
        exc_type = type(exc).__name__
        exc_msg = str(exc)
        trace = traceback.format_exc()

        self.logger.error(f"捕获到异常 {exc_type}: {exc_msg}")
        self.logger.debug(f"异常堆栈追踪:\n{trace}")

    def __enter__(self) -> "ExceptionHandler":
        """上下文管理器入口喵～

        Returns:
            异常处理器实例
        """
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        """上下文管理器退出喵～

        Args:
            exc_type: 异常类型
            exc_val: 异常值
            exc_tb: 异常追踪信息

        Returns:
            是否处理了异常
        """
        if exc_val is not None:
            return self.handle(exc_val)
        return False


class ApplicationError(Exception):
    """应用基础异常类喵～"""

    def __init__(self, message: str, code: int = 1) -> None:
        """初始化应用异常喵～

        Args:
            message: 异常消息
            code: 异常代码
        """
        self.message = message
        self.code = code
        super().__init__(message)


class ConfigError(ApplicationError):
    """配置错误异常喵～"""

    def __init__(self, message: str, code: int = 2) -> None:
        """初始化配置错误异常喵～

        Args:
            message: 错误消息
            code: 错误代码
        """
        super().__init__(f"配置错误: {message}", code)


class ValidationError(ApplicationError):
    """验证错误异常喵～"""

    def __init__(self, message: str, code: int = 3) -> None:
        """初始化验证错误异常喵～

        Args:
            message: 错误消息
            code: 错误代码
        """
        super().__init__(f"验证错误: {message}", code)


class ServiceError(ApplicationError):
    """服务错误异常喵～"""

    def __init__(self, message: str, code: int = 4) -> None:
        """初始化服务错误异常喵～

        Args:
            message: 错误消息
            code: 错误代码
        """
        super().__init__(f"服务错误: {message}", code)
