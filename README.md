# PySide6 Code Tutorial

用代码实例讲解 PySide6 ！

![GitHub Repo stars](https://img.shields.io/github/stars/muziing/PySide6-Code-Tutorial)
![GitHub forks](https://img.shields.io/github/forks/muziing/PySide6-Code-Tutorial)
![License](https://img.shields.io/github/license/muziing/PySide6-Code-Tutorial)
![GitHub Last Commit](https://img.shields.io/github/last-commit/muziing/PySide6-Code-Tutorial)

[![PySide Version](https://img.shields.io/badge/PySide-6.3-blue)](https://doc.qt.io/qtforpython/index.html)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

## 简介

之前的 [PyQt-Practice](https://github.com/muziing/PyQt_practice) 项目得到不少好评，目前已有 ![PyQt-Practice Stars](https://img.shields.io/github/stars/muziing/PyQt_practice.svg) 个 Stars。本项目沿用其形式，讲解介绍 **PySide6**。

- 代码中有较详细的注释作为讲解
- 几乎每个模块（`.py`文件）都可独立运行，展示了各种控件的各种功能属性作用
- 在自己的机器上实际运行一下，仔细观察一下每个属性值的改变会怎样影响控件的外观行为，可能比静态的文档教程更有效
- 相比 [PyQt-Practice](https://github.com/muziing/PyQt_practice)，改进了项目目录结构，更加清晰丰富

希望本项目对你我的 Python-GUI 学习之旅有所帮助。

## 如何使用

### 获取源代码

1. Star 本仓库
2. 通过以下方法之一，获取源码
    1. 克隆仓库（推荐）：`git clone https://github.com/muziing/PySide6-Code-Tutorial.git`
    2. 下载 zip：<https://github.com/muziing/PySide6-Code-Tutorial/archive/refs/heads/main.zip>
    3. 查看 [Releases](https://github.com/muziing/PySide6-Code-Tutorial/releases) 界面，下载最新发布版（文件更小）
3. 进入项目目录

### 配置虚拟环境与安装依赖

**方式 A** ：[Poetry](https://python-poetry.org/)（推荐）

1. 确保 Python 版本与 [pyproject.toml](./pyproject.toml) 中要求的一致
2. 按[官方文档](https://python-poetry.org/docs/#installation)提示安装 Poetry
3. 创建虚拟环境：`poetry env use /full/path/to/python`（注意替换路径）
4. 安装依赖：`poetry install --no-dev`
5. 使用该虚拟环境： `poetry shell`（或在 PyCharm 等 IDE 中配置）

> 更多 Poetry 使用方法信息，请参阅其[官方文档](https://python-poetry.org/docs/)。

**方式 B** ：其他包管理工具

1. 使用你喜欢的其他工具创建虚拟环境
2. `pip install -r requirements.txt`

### 运行与学习

1. 打开感兴趣的 `.py` 模块，运行
2. 观察该界面/控件效果
3. 阅读代码中的注释，可根据提示对特定行进行「注释/取消注释」
4. 再次运行该模块，观察变化

## 项目结构

TODO 定义项目结构

## 贡献

PySide6 Code Tutorial 是一个开源项目，非常期待以及感谢你的参与贡献。共同完善这个项目，让它帮助到更多人。

贡献的方式有很多种，并不一定都需要高超的编程能力：

- 指出错别字、错误拼写等
- 提议加入新功能、新模块等
- 参与某个 QWidget 控件相关代码编写
- 投稿优质 PySide6 相关博文、QSS 样式等
- ……

关于为本项目提交贡献的详细信息，请查阅[贡献指南](./CONTRIBUTING.md)。

## 开源许可与分享约定

本仓库使用 [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) 许可开源。对本项目的复制、分发和修改，请严格遵守该协议。

为便于使用者在自己的项目或博客文章中使用本仓库的代码片段，作以下分享约定：

| 类型           | 代码行数   | 来自模块           | 使用要求                                                                      |
|--------------|--------|----------------|---------------------------------------------------------------------------|
| 少量代码         | < 100  | 单个 `.py` 模块    | 直接复制使用即可，无需声明                                                             |
| 短片段          | < 500  | 6 个以内 `.py` 模块 | 在代码首行添加 `# 来自 github.com/muziing/PySide6-Code-Tutorial` 注释；如对代码有修改则必须明确声明 |
| 基于本项目修改衍生的项目 | \> 500 | 多个 `.py` 模块    | 严格遵守 GPLv3 相关要求                                                           |

## 打赏与捐助

本项目的主要作者/维护者是一名还没有收入的在校学生，如果本项目对你有帮助，希望可以请他喝一杯冰可乐 :beer:。

![微信收款码](./Resources/Images/muzing-WeChat-Collection-QRCode.png)
