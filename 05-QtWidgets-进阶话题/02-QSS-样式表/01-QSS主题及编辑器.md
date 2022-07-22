# QSS 主题与编辑器

> 本文转载自 [使用QSS美化PyQt界面 - muzing's](https://muzing.top/posts/28a1d80f/)

QSS 全称 Qt Style Sheets（Qt样式表），用于美化 Qt 程序界面，类似于 CSS，但不如 CSS 强大，选择器和属性较少。

本文介绍在 PySide6 中使用 QSS，但同样适用于 PyQt6、PyQt5、PySide2 等。

本文主要介绍 QSS 的加载使用以及分享，QSS 本身的语法详解请参考官方文档和其他教程。

## 官方文档

[Customizing Qt Widgets Using Style Sheets](https://doc.qt.io/qt-6/stylesheet-customizing.html)

[Qt Style Sheets Reference](https://doc.qt.io/qt-6/stylesheet-reference.html)

官方参考文档才是最官方全面的文档，有时间最好仔细阅读一下。

主要包括：

- 可应用样式表的控件列表
- 属性列表
- 图标列表
- 属性值列表
- 伪类选择器列表
- 子控件控制列表

内容非常多，在此就不展开了。

## 基本语法

类似 CSS，QSS 每一条都是由一个选择器和一组声明构成：

选择器选出要对哪种控件进行样式修改，

每个声明都是键值对，键为属性，值为属性值

![QSS语法](https://oss.muzing.top/image/QSS_eg.png)

## 使用方式

为降低耦合，往往把 QSS 写在一个单独的style.qss文件中，然后在 `main.py` 的 `QApplication` 或 `QMainWindow` 中加载样式

### 编写QSS

新建一个扩展名为`.qss`的文件，如style.qss，编辑内容。（本文后面有完整的样式主题、QSS 编辑器推荐）

把写好的 `.qss` 添加到 `qrc` 中

### 加载QSS

创建一个加载QSS样式表的公共类：

```python
class QSSLoader:
    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        with open(qss_file_name, 'r',  encoding='UTF-8') as file:
            return file.read()
```

在代码中加载qss样式表：

```python
app = QApplication(sys.argv)
window = MainWindow()
 
style_file = './style.qss'
style_sheet = QSSLoader.read_qss_file(style_file)
window.setStyleSheet(style_sheet)

window.show()
sys.exit(app.exec_())
```

## QSS 样式分享

### Qt 官方例子

[Qt Style Sheets Examples](https://doc.qt.io/qt-5/stylesheet-examples.html)

Qt官方给出的一些小例子，不一定好看但有很强的学习参考性

### Qt-Material

[UN-GCPDS/qt-material](https://github.com/UN-GCPDS/qt-material)

> This is another stylesheet for **PySide6**, **PySide2** and **PyQt5**, which looks like Material Design (close enough).

“一个仿Material的样式，适用于PySide6, PySide2以及PyQt5”

![浅色主题演示](https://oss.muzing.top/image/Qt-Material-light.gif)

![深色主题演示](https://oss.muzing.top/image/Qt-Material-dark.gif)

使用这套样式表也非常简单，作者已经打包发布到了pypi，所以我们只需要

```shell
pip install qt-material
```

安装，并在代码中import即可

```python
# 使用例子
import sys
# from PySide6 import QtWidgets
# from PySide2 import QtWidgets
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
apply_stylesheet(app, theme='dark_teal.xml')

# run
window.show()
app.exec_()
```

更多详细内容请查阅[该项目的README](https://github.com/UN-GCPDS/qt-material/blob/master/README.md)

### qtmodern

[GitHub 首页](https://github.com/gmarull/qtmodern)

![qtmodern](https://oss.muzing.top/image/qtmodern_mainwindow.png)

该库也已经添加至 PyPI，可以通过 pip 安装使用：

```shell
pip install qtmodern
```

```python
import qtmodern.styles
import qtmodern.windows

...

app = QApplication()
win = YourWindow()

qtmodern.styles.dark(app)
mw = qtmodern.windows.ModernWindow(win)
mw.show()

...

```

### PyDracula

[GitHub 首页](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6)

[YouTube 演示与教程](https://youtu.be/9DnaHg4M_AM)

注意此项目对应 **PySide6 / PyQt6** ，而不是 PyQt5

![PyDracula 深色主题](https://oss.muzing.top/image/PyDracula_dark.png)

![PyDracula 浅色主题](https://oss.muzing.top/image/PyDracula_light.png)

一个现代化的 GUI ，对高 DPI 有更好支持：

> Qt Widgets 是一项老技术，对高 DPI 设置没有很好的支持，当您的系统应用 DPI 高于 100% 时，这些图像看起来会失真。 通过在 Qt 模块导入正下方的“main.py”中应用以下代码，您可以使用一种变通方法来最小化此问题。

```python
# ADJUST QT FONT DPI FOR HIGHT SCALE
# ////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96"
```

### PyOneDark

[GitHub 首页](https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI)

[YouTube 展示视频](https://youtu.be/1v5errwE8ew)

和上面的 PyDracula 是同一作者

同样是对应 **PySide6** 的

![PyOneDark](https://oss.muzing.top/image/PyOneDark-Qt-Widgets-Modern-GUI.png)

该作者还有一个 [Simple_PySide_Base](https://github.com/Wanderson-Magalhaes/Simple_PySide_Base) 的仓库，对 PySide2 或 PyQt5 初学者如何创建一个美观的 GUI 程序是不错的参考

### PyQtDarkTheme

[GitHub 首页](https://github.com/5yutan5/PyQtDarkTheme)

- 扁平风格的深色/浅色主题
- 支持 PySide 与 PyQt
- 支持 PyInstaller
- 解决了 Qt 版本间的风格差异
- 深色和浅色主题的 QPalette

![PyQtDarkTheme-深色主题](https://oss.muzing.top/image/PyQtDarkTheme_widget_gallery_dark.png)

![PyQtDarkTheme-浅色主题](https://oss.muzing.top/image/PyQtDarkTheme_widget_gallery_light.png)

此主题的详细使用方法请参考[文档](https://github.com/5yutan5/PyQtDarkTheme#usage)

### 飞扬青云-QSS

在飞扬青云的 [QWidgetDemo](https://github.com/feiyangqingyun/QWidgetDemo) 项目中的 [styledemo](https://github.com/feiyangqingyun/QWidgetDemo/tree/master/styledemo) 子项目包含了3套很好看的QSS样式

![PS黑色](https://oss.muzing.top/image/feiyangqingyun_styledemo_psblack.png)

![浅蓝色](https://oss.muzing.top/image/feiyangqingyun_styledemo_lightblue.png)

![扁平化白色](https://oss.muzing.top/image/feiyangqingyun_styledemo_flatwhite.png)

[QSS目录链接](https://github.com/feiyangqingyun/QWidgetDemo/tree/master/styledemo/other)

### QDarkStyleSheet

> The most complete dark/light style sheet for Qt applications

“最完整的深色/浅色Qt主题”

- [文档](https://qdarkstylesheet.readthedocs.io/)

- [GitHub](https://github.com/ColinDuquesnoy/QDarkStyleSheet)

![containers_no_tabs_buttons](https://oss.muzing.top/image/qdarkstylesheet-containers_no_tabs_buttons.png)

![containers_no_tabs_buttons1](https://oss.muzing.top/image/qdarkstylesheet-containers_no_tabs_buttons1.png)

![containers_tabs_displays](https://oss.muzing.top/image/qdarkstylesheet-containers_tabs_displays.png)

![widgets_inputs_fields1](https://oss.muzing.top/image/qdarkstylesheet-widgets_inputs_fields1.png)

也可以通过pip直接安装使用

```shell
pip install qdarkstyle
```

```python
# PyQt5 使用例子
import sys
import qdarkstyle
from PyQt5 import QtWidgets

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# or in new API
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

# run
window.show()
app.exec_()
```

### GTRONICK-QSS

[GTRONICK/QSS: QT Style Sheets templates](https://github.com/GTRONICK/QSS)

一组QSS样式

![Ubuntu](https://oss.muzing.top/image/GTRONICK_QSS_Ubuntu.png)

![MaterialDark](https://oss.muzing.top/image/GTRONICK_QSS_MaterialDark.png)

![ElegantDark](https://oss.muzing.top/image/GTRONICK_QSS_ElegantDark.png)

![Aqua](https://oss.muzing.top/image/GTRONICK_QSS_Aqua.png)

![AMOLED](https://oss.muzing.top/image/GTRONICK_QSS_AMOLED.png)

## PyQt 图标库

### QtAwesome

[GitHub 主页](https://github.com/spyder-ide/qtawesome)

> QtAwesome enables iconic fonts such as Font Awesome and Elusive Icons in PyQt and PySide applications.
>
> It started as a Python port of the [QtAwesome](https://github.com/Gamecreature/qtawesome) C++ library by Rick Blommers.

可以通过 `conda` 或者 `pip` 安装

```shell
conda install qtawesome
```

```shell
pip install qtawesome
```

![QtAwesome 截图](https://oss.muzing.top/image/qtawesome-screenshot.gif)

QtAwesome 还附带一个图标浏览器，可以显示所有可用的图标。你可以使用它来搜索适合需求的图标，然后复制应该用于创建该图标的名称到代码中以应用图标

![QtAwesome 图标浏览器](https://oss.muzing.top/image/qtawesome-browser.png)

## QSS 编辑器

如果对上面推荐的这几个主题还不满意，你可以设计自己的QSS，下面推荐一些专用编辑器

### QssStylesheetEditor

[GitHub首页](https://github.com/hustlei/QssStylesheetEditor)

[中文README](https://github.com/hustlei/QssStylesheetEditor/blob/master/readme_zh-CN.md)

> QssStylesheetEditor 是一个功能强大的 Qt 样式表(QSS)编辑器，支持实时预览，自动提示，自定义变量, 支持预览自定义ui代码，引用QPalette等功能。

![程序主界面](https://oss.muzing.top/image/QssStylesheetEditor_GUI(v1.7).png)

![自动补全功能](https://oss.muzing.top/image/QssStylesheetEditor_AutoComplete.png)

这个软件有如下特点：

- Qss代码高亮，代码折叠
- Qss代码自动提示，自动补全
- 实时预览 Qss 样式效果，可以预览几乎所有的 qtwidget 控件效果
- 支持预览自定义界面代码
- 支持在 Qss 中自定义变量
- 自定义变量可以在颜色对话框中拾取变量的颜色
- 支持通过颜色对话框改变QPalette，并在Qss中引用
- 支持相对路径引用图片，以及引用资源文件中的图片
- 支持切换不同的系统 theme，如 xp 主题，vista 主题等(不同 theme 下 qss 效果会略有差异)
- 能够在 windows，linux，unix 上运行
- 支持多国语言（目前已有中文，英文，俄文翻译）

还有许多强大而实用的功能，可以在[README](https://github.com/hustlei/QssStylesheetEditor/blob/master/readme_zh-CN.md)中查看

### QSS Editor

> 🎨 Cross-platform application to edit and preview Qt style sheets (QSS).

跨平台的QSS编辑/预览应用

[GitHub主页](https://github.com/HappySeaFox/qsseditor)

[GitHub realeases](https://github.com/HappySeaFox/qsseditor/releases)

[下载地址2](https://sourceforge.net/projects/qsseditor/)

![qsseditor-1](https://oss.muzing.top/image/qsseditor-1.png)

![qsseditor-2](https://oss.muzing.top/image/qsseditor-2.png)

### Pycharm、VScode 插件

在Pycharm中可以安装 [Qt Style Sheet Highlighter](https://plugins.jetbrains.com/plugin/13963-qt-style-sheet-highlighter) 插件，提供对QSS的代码高亮功能

![Qt Style Sheet Highlighter](https://oss.muzing.top/image/20210716085119.png)

![Qt Style Sheet Highlighter 演示](https://oss.muzing.top/image/qss-highlighter-screen-plugin-screen.gif)

在VScode里可以安装 [Qt for Python](https://marketplace.visualstudio.com/items?itemName=seanwu.vscode-qt-for-python) 插件，该插件不仅支持qss文件的代码高亮，还支持qml、qrc、pro等代码的高亮

![Qt for Python](https://oss.muzing.top/image/20210714180428.png)
