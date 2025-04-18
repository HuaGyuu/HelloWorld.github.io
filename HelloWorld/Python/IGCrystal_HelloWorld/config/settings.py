"""应用设置管理模块喵～负责所有配置的加载和访问。"""

import os
from typing import Any, Dict, Optional

import yaml


class Settings:
    """设置管理类，处理所有配置喵～"""

    DEFAULT_CONFIG = {
        "application": {
            "name": "SuperComplexHelloWorld",
            "version": "1.0.0",
            "author": "喵娘",
            "description": "一个超级复杂的Hello World应用喵～",
        },
        "display": {
            "message": "Hello World",
            "color": "rainbow",
            "font": "default",
            "animation": True,
            "delay": 0.1,
        },
        "logging": {
            "file": "hello_world.log",
            "rotation": "10 MB",
            "retention": "1 week",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "advanced": {
            "use_threads": True,
            "max_retries": 3,
            "timeout": 5.0,
            "enable_cache": True,
        },
    }

    def __init__(self, config_name: str = "default") -> None:
        """初始化设置管理器喵～

        Args:
            config_name: 配置文件名称，默认为"default"
        """
        self.config_name = config_name
        self.config_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config"
        )
        self._config_data = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """加载配置文件，如果不存在则使用默认配置喵～

        Returns:
            配置数据字典
        """
        config_path = os.path.join(self.config_dir, f"{self.config_name}.yaml")

        # 尝试加载YAML配置
        if os.path.exists(config_path):
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    return yaml.safe_load(f)
            except Exception as e:
                print(f"加载配置文件失败: {str(e)}，使用默认配置喵～")

        # 如果没有配置文件或加载失败，使用默认配置
        return self.DEFAULT_CONFIG

    def get(self, section: str, key: Optional[str] = None, default: Any = None) -> Any:
        """获取配置值喵～

        Args:
            section: 配置节
            key: 配置键，如果为None则返回整个节
            default: 默认值，当配置不存在时返回

        Returns:
            配置值或默认值
        """
        if section not in self._config_data:
            return default

        if key is None:
            return self._config_data[section]

        return self._config_data[section].get(key, default)

    def get_all(self) -> Dict[str, Any]:
        """获取所有配置喵～

        Returns:
            所有配置数据
        """
        return self._config_data

    def save(self) -> bool:
        """保存当前配置到文件喵～

        Returns:
            是否保存成功
        """
        config_path = os.path.join(self.config_dir, f"{self.config_name}.yaml")
        try:
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            with open(config_path, "w", encoding="utf-8") as f:
                yaml.dump(self._config_data, f, default_flow_style=False)
            return True
        except Exception:
            return False
