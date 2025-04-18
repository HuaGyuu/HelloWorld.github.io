"""消息模型测试，测试消息数据类的功能喵～"""

import json
import os
import sys
import unittest
from datetime import datetime

# 添加项目根目录到系统路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.message import Message


class TestMessage(unittest.TestCase):
    """消息类测试喵～"""

    def setUp(self) -> None:
        """测试准备喵～"""
        self.content = "Hello World"
        self.color = "blue"
        self.font = "arial"
        self.animated = True
        self.metadata = {"version": "1.0.0", "author": "喵娘"}

        self.message = Message(
            content=self.content,
            color=self.color,
            font=self.font,
            animated=self.animated,
            metadata=self.metadata,
        )

    def test_create_message(self) -> None:
        """测试创建消息喵～"""
        self.assertEqual(self.message.content, self.content)
        self.assertEqual(self.message.color, self.color)
        self.assertEqual(self.message.font, self.font)
        self.assertEqual(self.message.animated, self.animated)
        self.assertEqual(self.message.metadata, self.metadata)
        self.assertIsInstance(self.message.created_at, datetime)

    def test_empty_content(self) -> None:
        """测试空内容喵～"""
        with self.assertRaises(ValueError):
            Message(content="")

    def test_to_dict(self) -> None:
        """测试转换为字典喵～"""
        message_dict = self.message.to_dict()
        self.assertEqual(message_dict["content"], self.content)
        self.assertEqual(message_dict["color"], self.color)
        self.assertEqual(message_dict["font"], self.font)
        self.assertEqual(message_dict["animated"], self.animated)
        self.assertEqual(message_dict["metadata"], self.metadata)
        self.assertIsInstance(message_dict["created_at"], str)

    def test_to_json(self) -> None:
        """测试转换为JSON喵～"""
        json_str = self.message.to_json()
        data = json.loads(json_str)
        self.assertEqual(data["content"], self.content)

    def test_from_dict(self) -> None:
        """测试从字典创建喵～"""
        message_dict = {
            "content": "Test Content",
            "color": "red",
            "font": "default",
            "animated": False,
            "created_at": datetime.now().isoformat(),
            "metadata": {"test": "value"},
        }

        message = Message.from_dict(message_dict)
        self.assertEqual(message.content, "Test Content")
        self.assertEqual(message.color, "red")
        self.assertEqual(message.metadata["test"], "value")

    def test_from_json(self) -> None:
        """测试从JSON创建喵～"""
        json_data = json.dumps(
            {
                "content": "JSON Content",
                "color": "green",
                "font": "default",
                "animated": True,
                "created_at": datetime.now().isoformat(),
                "metadata": {"source": "json"},
            }
        )

        message = Message.from_json(json_data)
        self.assertEqual(message.content, "JSON Content")
        self.assertEqual(message.color, "green")
        self.assertEqual(message.metadata["source"], "json")


if __name__ == "__main__":
    unittest.main()
