#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""超级复杂的Hello World项目入口喵～这个程序非常稳健哦～"""

import argparse
import logging
import os
import sys
from typing import Any, Dict, Optional

# 添加当前目录到系统路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from config.settings import Settings
from core.application import Application
from core.exception_handler import ExceptionHandler
from core.logger import LoggerFactory


def parse_arguments() -> argparse.Namespace:
    """解析命令行参数喵～

    Returns:
        解析后的命令行参数
    """
    parser = argparse.ArgumentParser(description="超级复杂的Hello World应用喵～")
    parser.add_argument("--debug", action="store_true", help="启用调试模式")
    parser.add_argument("--config", type=str, default="default", help="配置文件名")
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="日志级别",
    )
    return parser.parse_args()


def main() -> int:
    """主函数，执行应用并返回退出码喵～

    Returns:
        退出码：0表示成功，1表示失败
    """
    try:
        # 解析参数
        args = parse_arguments()

        # 初始化日志
        logger = LoggerFactory.get_logger(log_level=args.log_level)
        logger.info("启动超级复杂的Hello World应用喵～")

        # 初始化异常处理器
        exception_handler = ExceptionHandler(logger)

        # 加载配置
        settings = Settings(config_name=args.config)

        # 初始化应用
        with exception_handler:
            app = Application(settings=settings, logger=logger, debug=args.debug)
            app.initialize()
            app.run()
            app.cleanup()

        logger.info("应用执行完成，正常退出喵～")
        return 0

    except Exception as e:
        if "logger" in locals():
            logger.critical(f"发生未处理的异常: {str(e)}")
        else:
            print(f"启动失败: {str(e)}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
