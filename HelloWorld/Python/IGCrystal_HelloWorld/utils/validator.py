"""验证工具，提供数据验证相关功能喵～"""

import json
import os
import re
from typing import Any, Dict, List, Optional, Union


class Validator:
    """验证工具类喵～"""

    @staticmethod
    def is_valid_message(message: str) -> bool:
        """检查消息是否有效喵～

        Args:
            message: 要验证的消息

        Returns:
            消息是否有效
        """
        if not message or not isinstance(message, str):
            return False

        # 消息长度检查
        if len(message) > 1000:
            return False

        # 不允许全是空白字符
        if message.isspace():
            return False

        return True

    @staticmethod
    def is_valid_color(color: str) -> bool:
        """检查颜色是否有效喵～

        Args:
            color: 要验证的颜色

        Returns:
            颜色是否有效
        """
        if not color or not isinstance(color, str):
            return False

        # 检查是否是预定义颜色名称
        valid_color_names = [
            "red",
            "green",
            "blue",
            "yellow",
            "cyan",
            "magenta",
            "white",
            "black",
            "rainbow",
            "plain",
            "fancy",
            "box",
            "kawaii",
        ]

        if color.lower() in valid_color_names:
            return True

        # 检查是否是十六进制颜色代码
        hex_pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
        if re.match(hex_pattern, color):
            return True

        return False

    @staticmethod
    def is_valid_file_path(file_path: str) -> bool:
        """检查文件路径是否有效喵～

        Args:
            file_path: 要验证的文件路径

        Returns:
            文件路径是否有效
        """
        if not file_path or not isinstance(file_path, str):
            return False

        # 基本路径格式检查
        invalid_chars = set('<>:"|?*')
        if any(char in invalid_chars for char in file_path):
            return False

        # 检查目录是否存在
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            return False

        return True

    @staticmethod
    def is_valid_number(
        value: Any, min_value: Optional[float] = None, max_value: Optional[float] = None
    ) -> bool:
        """检查是否是有效数字喵～

        Args:
            value: 要验证的值
            min_value: 最小值限制
            max_value: 最大值限制

        Returns:
            是否是有效数字
        """
        try:
            num = float(value)

            if min_value is not None and num < min_value:
                return False

            if max_value is not None and num > max_value:
                return False

            return True

        except (ValueError, TypeError):
            return False

    @staticmethod
    def is_valid_json(json_str: str) -> bool:
        """检查是否是有效的JSON字符串喵～

        Args:
            json_str: 要验证的JSON字符串

        Returns:
            是否是有效的JSON
        """
        try:
            json.loads(json_str)
            return True
        except Exception:
            return False

    @staticmethod
    def validate_settings(settings: Dict[str, Any], required_keys: List[str]) -> List[str]:
        """验证设置，返回缺失的键喵～

        Args:
            settings: 设置字典
            required_keys: 必需的键列表

        Returns:
            缺失的键列表
        """
        missing = []
        for key in required_keys:
            if key not in settings:
                missing.append(key)
        return missing
