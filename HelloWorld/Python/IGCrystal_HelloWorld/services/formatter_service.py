"""格式化服务，处理消息的格式化和样式应用喵～"""

import random
from typing import Any, Callable, Dict, List, Optional, Tuple

from config.constants import Constants
from config.settings import Settings
from models.message import Message
from utils.string_utils import StringUtils


class FormatterService:
    """格式化服务类喵～"""

    def __init__(self, settings: Settings) -> None:
        """初始化格式化服务喵～

        Args:
            settings: 应用配置
        """
        self.settings = settings
        self._load_formatters()

    def _load_formatters(self) -> None:
        """加载格式化器喵～"""
        self.formatters: Dict[str, Callable[[str], str]] = {
            "plain": self._format_plain,
            "fancy": self._format_fancy,
            "rainbow": self._format_rainbow,
            "box": self._format_box,
            "kawaii": self._format_kawaii,
        }

    def format_message(self, message: Message) -> str:
        """格式化消息喵～

        Args:
            message: 要格式化的消息

        Returns:
            格式化后的消息文本
        """
        # 根据颜色选择格式化器
        formatter = self.formatters.get(message.color, self._format_plain)

        # 应用格式化
        return formatter(message.content)

    def _format_plain(self, content: str) -> str:
        """普通格式化喵～

        Args:
            content: 消息内容

        Returns:
            格式化后的文本
        """
        return content

    def _format_fancy(self, content: str) -> str:
        """花哨格式化喵～

        Args:
            content: 消息内容

        Returns:
            格式化后的文本
        """
        stars = "✨" * (len(content) // 5 + 2)
        return f"{stars} {content} {stars}"

    def _format_rainbow(self, content: str) -> str:
        """彩虹格式化（在终端中会更好看）喵～

        Args:
            content: 消息内容

        Returns:
            格式化后的文本
        """
        # 模拟彩虹效果
        rainbow_prefix = "🌈 "
        rainbow_suffix = " 🌈"
        return f"{rainbow_prefix}{content}{rainbow_suffix}"

    def _format_box(self, content: str) -> str:
        """盒子格式化喵～

        Args:
            content: 消息内容

        Returns:
            格式化后的文本
        """
        width = len(content) + 4
        top_bottom = "+" + "-" * (width - 2) + "+"
        return f"{top_bottom}\n|  {content}  |\n{top_bottom}"

    def _format_kawaii(self, content: str) -> str:
        """可爱风格格式化喵～

        Args:
            content: 消息内容

        Returns:
            格式化后的文本
        """
        return f"ฅ^•ﻌ•^ฅ {content} (=^･ω･^=)"

    def apply_style(self, content: str, style: str) -> str:
        """应用指定样式喵～

        Args:
            content: 消息内容
            style: 样式名称

        Returns:
            应用样式后的文本
        """
        if style in self.formatters:
            return self.formatters[style](content)
        return content

    def get_available_styles(self) -> List[str]:
        """获取所有可用的样式喵～

        Returns:
            样式名称列表
        """
        return list(self.formatters.keys())

    def random_style(self, content: str) -> str:
        """应用随机样式喵～

        Args:
            content: 消息内容

        Returns:
            应用随机样式后的文本
        """
        style = random.choice(list(self.formatters.keys()))
        return self.apply_style(content, style)
