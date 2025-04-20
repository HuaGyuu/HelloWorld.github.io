"""消息模型，定义Hello World消息的数据结构喵～"""

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class Message:
    """消息数据类喵～"""

    content: str
    color: str = "white"
    font: str = "default"
    animated: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """初始化后的处理喵～

        Raises:
            ValueError: 当消息内容为空或非字符串时抛出
        """
        # 验证内容不为空
        if not self.content or not isinstance(self.content, str):
            raise ValueError("消息内容不能为空，而且必须是字符串喵！")

        # 设置默认元数据
        if "version" not in self.metadata:
            self.metadata["version"] = "1.0.0"

        if "type" not in self.metadata:
            self.metadata["type"] = "text"

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典喵～

        Returns:
            包含消息信息的字典
        """
        result = asdict(self)
        # 将datetime转换为ISO格式字符串
        result["created_at"] = self.created_at.isoformat()
        return result

    def to_json(self) -> str:
        """转换为JSON字符串喵～

        Returns:
            表示消息的JSON字符串
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Message":
        """从字典创建消息对象喵～

        Args:
            data: 包含消息信息的字典

        Returns:
            创建的消息实例
        """
        # 处理日期时间字段
        if "created_at" in data and isinstance(data["created_at"], str):
            data["created_at"] = datetime.fromisoformat(data["created_at"])
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> "Message":
        """从JSON字符串创建消息对象喵～

        Args:
            json_str: 包含消息信息的JSON字符串

        Returns:
            创建的消息实例
        """
        data = json.loads(json_str)
        return cls.from_dict(data)

    def __str__(self) -> str:
        """字符串表示喵～

        Returns:
            消息的简短字符串表示
        """
        return f"Message({self.content}, color={self.color}, animated={self.animated})"

    def __repr__(self) -> str:
        """对象表示喵～

        Returns:
            消息的详细字符串表示
        """
        return (
            f"Message(content='{self.content}', color='{self.color}', "
            f"font='{self.font}', animated={self.animated})"
        )
