# 贡献指南

非常感谢你愿意为 PySide6-Code-Tutorial 项目提供贡献，请阅读以下内容，遵守一些基本规则，以便项目保持良好状态快速发展。

## 开始编码之前

如果你准备对代码进行超过数十行的修改或新增，我强烈建议你先提交一个 issue，谈谈你想实现的东西。在投入很多精力之前，我们应该先讨论一下是否要这样做，也可以确保我们不重复工作。

## 编写代码

### 准备开发环境

开发环境相较于使用环境较为复杂，确保已经安装 Python 3.11+ 和 [Poetry](https://python-poetry.org/docs/#installation)，然后通过 Poetry 创建和安装开发环境：

```shell
cd PySide6-Code-Tutorial
poetry init
poetry install
```

还需要通过 [pre-commit](https://pre-commit.com/) 安装 git 钩子：

```shell
pre-commit install
```

### 代码风格

- 总体来讲，新增和修改的代码应接近原有代码的风格。尽量使代码有良好的可读性。
- 请使用 [Black](https://black.readthedocs.io/en/stable/) 格式化代码，确保所有代码风格与项目一致。开发环境中已经安装了 Black，配置使用方法可以参考[这篇文章](https://muzing.top/posts/a29e4743/)。
- 请为代码添加充分的[类型注解](https://muzing.top/posts/84a8da1c/)，并能通过 [mypy](https://mypy.readthedocs.io/en/stable/) 检查不报错。
- 请为模块、类、函数/方法、属性等添加 docstring 或注释，确保含义清晰易读。

## 拉取请求

新建一个指向 [muziing/PySide6-Code-Tutorial](https://github.com/muziing/PySide6-Code-Tutorial) 的 `main` 分支的拉取请求，我将尽快 review 代码并给出反馈。
