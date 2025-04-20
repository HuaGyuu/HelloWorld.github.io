"""消息服务，处理消息的生成、转换和管理喵～"""

import random
from typing import Any, Dict, List, Optional

from config.constants import Constants
from config.settings import Settings
from core.exception_handler import ServiceError
from models.message import Message


class MessageService:
    """消息服务类喵～"""

    def __init__(self, settings: Settings) -> None:
        """初始化消息服务喵～

        Args:
            settings: 应用配置
        """
        self.settings = settings
        self.message_cache: Dict[str, Message] = {}

    def create_message(
        self,
        content: Optional[str] = None,
        color: Optional[str] = None,
        animated: Optional[bool] = None,
    ) -> Message:
        """创建一个新消息喵～

        Args:
            content: 消息内容，默认使用配置中的消息
            color: 消息颜色，默认使用配置中的颜色
            animated: 是否动画显示，默认使用配置中的设置

        Returns:
            创建的消息对象

        Raises:
            ServiceError: 创建消息失败时抛出
        """
        # 使用提供的值或默认配置
        _content = content or self.settings.get(
            "display", "message", Constants.DEFAULT_MESSAGE
        )
        _color = color or self.settings.get("display", "color", "white")
        _animated = (
            animated
            if animated is not None
            else self.settings.get("display", "animation", True)
        )

        # 创建消息对象
        try:
            message = Message(content=_content, color=_color, animated=_animated)

            # 添加到缓存
            cache_key = f"{_content}_{_color}_{_animated}"
            self.message_cache[cache_key] = message

            return message

        except ValueError as e:
            raise ServiceError(f"创建消息失败: {str(e)}")

    def get_random_message(self) -> Message:
        """获取随机消息喵～

        Returns:
            随机创建的消息对象
        """
        content = random.choice(Constants.MESSAGE_VARIANTS)
        color = random.choice(list(Constants.COLORS.keys()))
        animated = random.choice([True, False])

        return self.create_message(content, color, animated)

    def transform_message(
        self, message: Message, new_content: Optional[str] = None, new_color: Optional[str] = None
    ) -> Message:
        """转换消息喵～

        Args:
            message: 原始消息
            new_content: 新的消息内容
            new_color: 新的消息颜色

        Returns:
            转换后的新消息对象
        """
        # 创建一个新的消息，保留原消息的其他属性
        return Message(
            content=new_content or message.content,
            color=new_color or message.color,
            font=message.font,
            animated=message.animated,
            metadata=message.metadata.copy(),
        )

    def save_message(self, message: Message, file_path: str) -> bool:
        """保存消息到文件喵～

        Args:
            message: 要保存的消息
            file_path: 保存路径

        Returns:
            是否保存成功

        Raises:
            ServiceError: 保存失败时抛出
        """
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(message.to_json())
            return True
        except Exception as e:
            raise ServiceError(f"保存消息失败: {str(e)}")

    def load_message(self, file_path: str) -> Message:
        """从文件加载消息喵～

        Args:
            file_path: 文件路径

        Returns:
            加载的消息对象

        Raises:
            ServiceError: 加载失败时抛出
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json_data = f.read()
            return Message.from_json(json_data)
        except Exception as e:
            raise ServiceError(f"加载消息失败: {str(e)}")
