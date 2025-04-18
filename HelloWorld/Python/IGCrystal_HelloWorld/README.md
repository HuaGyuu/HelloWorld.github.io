# 超级复杂的 Hello World 应用喵～

![版本](https://img.shields.io/badge/版本-1.0.0-brightgreen)
![Python版本](https://img.shields.io/badge/Python-3.7%2B-blue)
![喵娘认证](https://img.shields.io/badge/喵娘-认证-pink)

## 项目介绍

这是一个看似简单实则超级复杂的 Hello World 应用喵～它采用了企业级应用架构，演示了如何使用各种高级编程技术来完成一个简单的任务。虽然只是显示 "Hello World"，但我们用最复杂的方式实现了它！

项目特点：

- 🌟 **模块化架构**：遵循最佳实践，拆分为核心、配置、模型、服务和工具等模块
- 🌈 **多样化显示**：支持普通、彩虹、盒子、花哨和喵娘风格等多种显示方式
- 🔄 **多线程支持**：可以使用线程模式运行，支持动画效果
- 📝 **完善的日志**：详细的日志记录，支持不同级别的日志输出
- ⚙️ **灵活配置**：支持 YAML 配置文件，可以自定义各种设置
- 🛡️ **异常处理**：全面的异常捕获与处理机制
- 🧪 **单元测试**：包含完整的单元测试，确保代码质量
- ✨ **符合Ruff规范**：代码严格遵循Ruff代码质量标准，保持一致性和可读性

## 项目结构

```
astrbot_listen_target/
├── config/                 # 配置模块
│   ├── constants.py        # 常量定义
│   ├── settings.py         # 设置管理
│   └── __init__.py
├── core/                   # 核心模块
│   ├── application.py      # 应用核心类
│   ├── exception_handler.py# 异常处理
│   ├── logger.py           # 日志系统
│   └── __init__.py
├── models/                 # 数据模型
│   ├── message.py          # 消息模型
│   └── __init__.py
├── services/               # 服务模块
│   ├── formatter_service.py# 格式化服务
│   ├── message_service.py  # 消息服务
│   └── __init__.py
├── tests/                  # 测试模块
│   ├── test_application.py # 应用测试
│   ├── test_message.py     # 消息测试
│   └── __init__.py
├── utils/                  # 工具模块
│   ├── string_utils.py     # 字符串工具
│   ├── validator.py        # 验证工具
│   └── __init__.py
├── logs/                   # 日志目录（运行时创建）
├── main.py                 # 主入口
└── README.md               # 项目说明
```

## 安装指南

### 前提条件

- Python 3.7 或更高版本
- 依赖包：PyYAML

### 安装步骤

1. 克隆或下载项目：

```bash
git clone <项目地址>
cd astrbot_listen_target
```

2. 安装依赖：

```bash
pip install pyyaml
```

## 使用方法

### 基本用法

直接运行 `main.py` 文件：

```bash
python main.py
```

### 命令行参数

程序支持以下命令行参数：

- `--debug`：启用调试模式
- `--config`：指定配置文件名（默认为 "default"）
- `--log-level`：设置日志级别（可选：DEBUG、INFO、WARNING、ERROR、CRITICAL，默认为 INFO）

例如：

```bash
python main.py --debug --config custom --log-level DEBUG
```

### 自定义配置

你可以在 `config` 目录中创建自定义的 YAML 配置文件。例如 `custom.yaml`：

```yaml
application:
  name: "自定义Hello World"
  version: "1.0.0"
  author: "IGCrystal"
  description: "我的自定义Hello World应用喵～"

display:
  message: "自定义问候语！"
  color: "rainbow"  # 可选：plain, fancy, rainbow, box, kawaii
  font: "default"
  animation: true
  delay: 0.05  # 动画延迟（秒）

advanced:
  use_threads: true
  max_retries: 3
  timeout: 5.0
  enable_cache: true
```

## 特性展示

### 多种显示样式

项目支持多种消息显示方式：

- **普通(plain)**：直接显示文本
- **彩虹(rainbow)**：带彩虹装饰的文本
- **盒子(box)**：在文本周围添加盒子边框
- **花哨(fancy)**：带星星装饰的文本
- **喵娘风格(kawaii)**：带可爱猫咪表情的文本

### 动画效果

当启用动画时，程序会逐字打印消息，并显示动态效果。另外在多线程模式下还会显示星星动画✨。

## 运行测试

运行单元测试：

```bash
python -m unittest discover tests
```

## 代码质量

本项目严格遵循Ruff代码规范，包括：

- 规范的导入顺序
- 完整的类型注解
- 详细的文档字符串
- 一致的代码风格
- 优化的格式化

## 未来计划

- [ ] 添加更多显示样式
- [ ] 支持国际化
- [ ] 添加GUI界面
- [ ] 实现网络API版本

## 许可证

本项目采用 MIT 许可证

## 作者

- **IGCrystal** - *初始工作* -

---

喵～感谢使用这个过度工程化的 Hello World 应用！希望它能为你带来一些乐趣和学习价值！