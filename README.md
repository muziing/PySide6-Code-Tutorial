# PySide6 Code Tutorial

用代码实例讲解 PySide6 ！

![GitHub Repo stars](https://img.shields.io/github/stars/muziing/PySide6-Code-Tutorial)
![GitHub forks](https://img.shields.io/github/forks/muziing/PySide6-Code-Tutorial)
![License](https://img.shields.io/github/license/muziing/PySide6-Code-Tutorial)

![PySide Version](https://img.shields.io/badge/PySide-6.3-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## 简介

之前的 [PyQt-Practice](https://github.com/muziing/PyQt_practice) 项目得到不少好评，目前已有 ![PyQt-Practice Stars](https://img.shields.io/github/stars/muziing/PyQt_practice.svg) 个 Stars。本项目沿用其「以**附有丰富注释**的**可直接运行**的代码讲解知识」的形式，讲解介绍 PySide6。并改进了项目目录结构，更加清晰丰富。希望对你我的 Python-GUI 学习之旅有所帮助。

## 如何使用

### 获取源代码

1. Star 本仓库
2. 通过以下方法之一，获取源码
    1. 克隆仓库（推荐）：`git clone https://github.com/muziing/PySide6-Code-Tutorial.git`
    2. 下载 zip ：<https://github.com/muziing/PySide6-Code-Tutorial/archive/refs/heads/main.zip>
    3. 查看 [Releases](https://github.com/muziing/PySide6-Code-Tutorial/releases) 界面，下载最新发布版（文件更小）
3. 进入项目目录

### 配置虚拟环境与安装依赖

**方式 A** ：[Poetry](https://python-poetry.org/)（推荐）

1. 确保 Python 版本与 [pyproject.toml](./pyproject.toml) 中要求的一致
2. 按[官方文档](https://python-poetry.org/docs/#installation)提示安装 Poetry
3. 创建虚拟环境：`poetry env use /full/path/to/python`（注意替换路径）
4. 安装依赖：`poetry install`
5. 使用该虚拟环境： `poetry shell`（或在 PyCharm 等 IDE 中配置）

**方式 B**：其他包管理工具

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

PySide6 Code Tutorial 是一个开源项目，非常期待你的参与贡献，共同完善它。

> 推荐阅读：[如何为开源做贡献](https://opensource.guide/zh-hans/how-to-contribute/)

### 报告错误

如果在本项目中发现错误（不仅限于代码错误，也可以是文档、注释中的错别字等），请提交一个 [Issue](https://github.com/muziing/PySide6-Code-Tutorial/issues) 以报告该错误。

Issue 中请简洁而清晰地描述该错误的位置、问题、（可选）改进建议。

### 修复错误

如果你认为自己有能力修复某个已有的 [Issue](https://github.com/muziing/PySide6-Code-Tutorial/issues) 或刚刚发现的新问题，请按如下流程进行：

1. （对于新发现的错误）提交一个 Issue，描述其位置、问题
2. Fork 本仓库
3. 基于 `dev` 分支的最新提交，新建一个分支，名称为 `Fix #123` （其中 `123` 为 Issue 编号）
4. 在新分支中修复错误，提交一个 [Pull Request](https://github.com/muziing/PySide6-Code-Tutorial/pulls)
5. 经代码审核，确认无误后，该分支会被合并入 `dev` 分支，未来将并入 `main` 分支

### 贡献代码

TODO 贡献代码细则

注意事项：

1. 确保已在本地开发环境安装全部「开发依赖项」，详见 [pyproject.toml](./pyproject.toml) 中的 `[tool.poetry.dev-dependencies]`
2. 尽可能保证代码风格与现有代码一致

## 开源许可与分享约定

本仓库使用 [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) 许可开源。对本项目的复制、分发和修改，请严格遵守该协议。

为便于使用者在自己的项目/博客文章中使用本仓库的代码片段，作以下约定：

TODO 分享约定

## 打赏与捐助

本项目的主要作者/维护者是一名还没有收入的在校学生，如果本项目对你有帮助，希望可以请他喝一杯冰可乐 :beer:。

![微信收款码](./Resources/Images/muzing-WeChat-Collection-QRCode.png)
