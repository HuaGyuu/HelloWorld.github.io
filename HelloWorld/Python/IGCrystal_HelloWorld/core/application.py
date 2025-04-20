"""应用核心类，处理整个Hello World的主要逻辑喵～"""

import random
import threading
import time
from typing import Any, Callable, Dict, List, Optional

from config.constants import Constants, DisplayMode
from config.settings import Settings
from models.message import Message
from services.formatter_service import FormatterService
from services.message_service import MessageService
from utils.string_utils import StringUtils
from utils.validator import Validator


class Application:
    """超级复杂的Hello World应用核心喵～"""

    def __init__(self, settings: Settings, logger: Any, debug: bool = False) -> None:
        """初始化应用实例喵～

        Args:
            settings: 应用配置
            logger: 日志记录器
            debug: 是否开启调试模式
        """
        self.settings = settings
        self.logger = logger
        self.debug = debug
        self.message_service = MessageService(settings)
        self.formatter_service = FormatterService(settings)
        self._initialized = False
        self._running = False
        self._threads: List[threading.Thread] = []

    def initialize(self) -> None:
        """初始化应用喵～"""
        if self._initialized:
            self.logger.warning("应用已经初始化过了喵～")
            return

        self.logger.info("初始化应用...")

        # 获取配置
        self.use_threads = self.settings.get("advanced", "use_threads", False)
        self.enable_animation = self.settings.get("display", "animation", True)
        self.message_text = self.settings.get(
            "display", "message", Constants.DEFAULT_MESSAGE
        )

        # 验证设置
        if not Validator.is_valid_message(self.message_text):
            self.logger.warning(
                f"无效的消息格式: {self.message_text}，使用默认消息喵～"
            )
            self.message_text = Constants.DEFAULT_MESSAGE

        # 创建消息对象
        self.message = Message(
            content=self.message_text,
            color=self.settings.get("display", "color", "white"),
            font=self.settings.get("display", "font", "default"),
            animated=self.enable_animation,
        )

        self._initialized = True
        self.logger.info("应用初始化完成喵～")

    def run(self) -> None:
        """运行应用喵～

        Raises:
            RuntimeError: 应用未初始化时抛出
        """
        if not self._initialized:
            self.logger.error("应用未初始化，无法运行喵！")
            raise RuntimeError("Application not initialized")

        self.logger.info("开始运行应用喵～")
        self._running = True

        # 根据配置决定是否使用线程
        if self.use_threads:
            self._run_threaded()
        else:
            self._run_simple()

        self._running = False
        self.logger.info("应用运行完成喵～")

    def _run_simple(self) -> None:
        """简单模式运行喵～"""
        self.logger.debug("使用简单模式运行")

        # 获取并格式化消息
        formatted_message = self.formatter_service.format_message(self.message)

        # 显示消息
        delay = self.settings.get("display", "delay", 0.1)

        if self.enable_animation:
            self._display_animated(formatted_message, delay)
        else:
            self._display_simple(formatted_message)

    def _run_threaded(self) -> None:
        """线程模式运行喵～"""
        self.logger.debug("使用线程模式运行")

        # 创建任务线程
        display_thread = threading.Thread(
            target=self._thread_display_task,
            name="DisplayThread",
        )

        animation_thread = None
        if self.enable_animation:
            animation_thread = threading.Thread(
                target=self._thread_animation_task,
                name="AnimationThread",
                daemon=True,  # 设置为守护线程，这样主线程结束时它会自动终止喵～
            )

        # 启动线程
        self._threads.append(display_thread)
        display_thread.start()

        if animation_thread:
            self._threads.append(animation_thread)
            animation_thread.start()

        # 等待显示线程完成（只等待显示线程，不等待动画线程）
        display_thread.join()

        # 明确设置停止动画
        self._running = False

        # 给动画线程一个短暂的时间来结束
        if animation_thread and animation_thread.is_alive():
            animation_thread.join(timeout=0.5)

    def _thread_display_task(self) -> None:
        """显示线程任务喵～"""
        formatted_message = self.formatter_service.format_message(self.message)
        self._display_simple(formatted_message)

    def _thread_animation_task(self) -> None:
        """动画线程任务喵～"""
        if not self.enable_animation:
            return

        # 简单的动画效果
        delay = self.settings.get("display", "delay", 0.1)
        max_stars = 50  # 最多输出50个星星，防止无限输出喵～
        star_count = 0

        while self._running and star_count < max_stars:
            print("✨", end="", flush=True)
            time.sleep(delay)
            star_count += 1

        # 最后输出一个换行，保持输出美观喵～
        if star_count > 0:
            print()

    def _display_simple(self, message: str) -> None:
        """简单显示消息喵～

        Args:
            message: 要显示的消息
        """
        print("\n" + "=" * 50)
        print(f"{Constants.SPECIAL_CHARS[0]} {message} {Constants.SPECIAL_CHARS[0]}")
        print("=" * 50 + "\n")

    def _display_animated(self, message: str, delay: float) -> None:
        """带动画效果显示消息喵～

        Args:
            message: 要显示的消息
            delay: 动画延迟时间
        """
        # 打印边框
        print("\n" + "=" * 50)

        # 逐字打印消息
        print(f"{Constants.SPECIAL_CHARS[0]} ", end="", flush=True)
        for char in message:
            print(char, end="", flush=True)
            time.sleep(delay)

        print(f" {Constants.SPECIAL_CHARS[0]}")
        print("=" * 50 + "\n")

    def cleanup(self) -> None:
        """清理应用资源喵～"""
        self.logger.info("清理应用资源...")
        self._running = False

        # 等待所有非守护线程完成
        for thread in self._threads:
            if thread.is_alive() and not thread.daemon:
                thread.join(timeout=1.0)

        self._threads.clear()
        self.logger.info("应用资源清理完成喵～")

    def __str__(self) -> str:
        """返回应用的字符串表示喵～

        Returns:
            应用状态的字符串表示
        """
        return f"Application(initialized={self._initialized}, running={self._running})"
