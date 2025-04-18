"""应用常量定义喵～包含所有固定不变的值。"""

from enum import Enum, auto
from typing import Dict, List, Tuple


class LogLevel(Enum):
    """日志级别枚举喵～"""

    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class DisplayMode(Enum):
    """显示模式枚举喵～"""

    NORMAL = auto()
    FANCY = auto()
    MINIMAL = auto()
    VERBOSE = auto()


class ExitCode(Enum):
    """退出码枚举喵～"""

    SUCCESS = 0
    ERROR_GENERIC = 1
    ERROR_CONFIG = 2
    ERROR_RUNTIME = 3


class Constants:
    """应用常量喵～"""

    APP_NAME = "SuperComplexHelloWorld"
    VERSION = "1.0.0"
    AUTHOR = "喵娘"

    # 颜色定义 (RGB元组)
    COLORS = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "white": (255, 255, 255),
        "black": (0, 0, 0),
    }

    # 彩虹颜色序列
    RAINBOW_COLORS = [
        COLORS["red"],
        COLORS["yellow"],
        COLORS["green"],
        COLORS["cyan"],
        COLORS["blue"],
        COLORS["magenta"],
    ]

    # 动画类型
    ANIMATIONS = ["fade", "blink", "slide", "typewriter", "bounce"]

    # 默认消息
    DEFAULT_MESSAGE = "Hello World"

    # 消息变体
    MESSAGE_VARIANTS = [
        "你好，世界～",
        "Hello World!",
        "こんにちは世界！",
        "Bonjour le monde!",
        "¡Hola Mundo!",
        "Привет, мир!",
    ]

    # 超时设置（秒）
    DEFAULT_TIMEOUT = 5.0
    MAX_TIMEOUT = 30.0

    # 重试设置
    DEFAULT_RETRIES = 3
    MAX_RETRIES = 10

    # 文件路径
    DEFAULT_LOG_FILE = "hello_world.log"
    CONFIG_DIR = "config"

    # 特殊字符
    SPECIAL_CHARS = "✨🌟⭐🌈🐱"
