"""应用核心测试，测试应用核心功能喵～"""

import logging
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# 添加项目根目录到系统路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.settings import Settings
from core.application import Application
from models.message import Message


class TestApplication(unittest.TestCase):
    """应用类测试喵～"""

    def setUp(self) -> None:
        """测试准备喵～"""
        # 创建模拟的Settings对象
        self.mock_settings = MagicMock(spec=Settings)
        self.mock_settings.get.side_effect = self._mock_settings_get

        # 创建模拟的Logger对象
        self.mock_logger = MagicMock(spec=logging.Logger)

        # 创建应用实例
        self.app = Application(
            settings=self.mock_settings, logger=self.mock_logger, debug=True
        )

    def _mock_settings_get(
        self, section: str, key: str = None, default: object = None
    ) -> object:
        """模拟设置获取功能喵～

        Args:
            section: 配置节
            key: 配置键
            default: 默认值

        Returns:
            配置值
        """
        settings_data = {
            "display": {
                "message": "Test Hello World",
                "color": "blue",
                "animation": False,
                "delay": 0.01,
            },
            "advanced": {"use_threads": False},
        }

        if key is None:
            return settings_data.get(section, {})

        return settings_data.get(section, {}).get(key, default)

    def test_initialization(self) -> None:
        """测试初始化喵～"""
        self.assertFalse(self.app._initialized)
        self.assertFalse(self.app._running)

        self.app.initialize()

        self.assertTrue(self.app._initialized)
        self.assertFalse(self.app._running)
        self.assertEqual(self.app.message.content, "Test Hello World")
        self.assertEqual(self.app.message.color, "blue")
        self.assertFalse(self.app.message.animated)

    def test_run_without_init(self) -> None:
        """测试未初始化运行喵～"""
        with self.assertRaises(RuntimeError):
            self.app.run()

    @patch("builtins.print")
    def test_run_simple(self, mock_print: MagicMock) -> None:
        """测试简单运行喵～

        Args:
            mock_print: 模拟的print函数
        """
        self.app.initialize()
        self.app.run()

        self.mock_logger.info.assert_called()
        mock_print.assert_called()

    def test_cleanup(self) -> None:
        """测试清理喵～"""
        self.app.initialize()
        # 模拟线程
        mock_thread = MagicMock()
        mock_thread.is_alive.return_value = True
        self.app._threads = [mock_thread]

        self.app.cleanup()

        self.assertFalse(self.app._running)
        self.assertEqual(len(self.app._threads), 0)
        mock_thread.join.assert_called_once()


if __name__ == "__main__":
    unittest.main()
