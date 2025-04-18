"""字符串工具，提供字符串处理相关功能喵～"""

import random
import re
from typing import Any, Dict, List, Optional


class StringUtils:
    """字符串工具类喵～"""

    @staticmethod
    def truncate(text: str, max_length: int = 100, suffix: str = "...") -> str:
        """截断字符串到指定长度喵～

        Args:
            text: 原始文本
            max_length: 最大长度
            suffix: 截断后添加的后缀

        Returns:
            截断后的文本
        """
        if len(text) <= max_length:
            return text
        return text[: max_length - len(suffix)] + suffix

    @staticmethod
    def center_pad(text: str, width: int, fill_char: str = " ") -> str:
        """居中填充字符串喵～

        Args:
            text: 原始文本
            width: 目标宽度
            fill_char: 填充字符

        Returns:
            填充后的文本
        """
        if len(text) >= width:
            return text

        left_pad = (width - len(text)) // 2
        right_pad = width - len(text) - left_pad

        return fill_char * left_pad + text + fill_char * right_pad

    @staticmethod
    def remove_special_chars(text: str) -> str:
        """移除特殊字符喵～

        Args:
            text: 原始文本

        Returns:
            处理后的文本
        """
        return re.sub(r"[^\w\s]", "", text)

    @staticmethod
    def to_camel_case(text: str) -> str:
        """转换为驼峰命名喵～

        Args:
            text: 原始文本

        Returns:
            驼峰命名格式的文本
        """
        # 先转为snake_case确保格式统一
        s = re.sub(r"[^a-zA-Z0-9]", "_", text.lower())
        # 转换为camelCase
        camel = "".join(
            word.capitalize() if i > 0 else word for i, word in enumerate(s.split("_"))
        )
        return camel

    @staticmethod
    def generate_random_string(
        length: int = 10, include_digits: bool = True, include_special: bool = False
    ) -> str:
        """生成随机字符串喵～

        Args:
            length: 生成的字符串长度
            include_digits: 是否包含数字
            include_special: 是否包含特殊字符

        Returns:
            生成的随机字符串
        """
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if include_digits:
            charset += "0123456789"

        if include_special:
            charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        return "".join(random.choice(charset) for _ in range(length))

    @staticmethod
    def contains_any(text: str, substrings: List[str]) -> bool:
        """检查字符串是否包含任意子串喵～

        Args:
            text: 要检查的文本
            substrings: 子串列表

        Returns:
            是否包含任意子串
        """
        return any(sub in text for sub in substrings)

    @staticmethod
    def replace_all(text: str, replacements: Dict[str, str]) -> str:
        """替换多个子串喵～

        Args:
            text: 原始文本
            replacements: 替换映射（旧文本 -> 新文本）

        Returns:
            替换后的文本
        """
        result = text
        for old, new in replacements.items():
            result = result.replace(old, new)
        return result

    @staticmethod
    def add_kawaii(text: str) -> str:
        """添加可爱风格喵～

        Args:
            text: 原始文本

        Returns:
            添加可爱装饰后的文本
        """
        kawaii_prefixes = ["✨ ", "🌸 ", "💖 ", "🎀 "]
        kawaii_suffixes = [" ✨", " 💕", " 🌟", " 🐱"]

        prefix = random.choice(kawaii_prefixes)
        suffix = random.choice(kawaii_suffixes)

        return f"{prefix}{text}{suffix}"
