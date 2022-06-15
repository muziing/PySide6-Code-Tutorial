# 对象树与所有状态

> **翻译信息**：
>
> 本文翻译自 Qt6 官方文档 *[Object Trees & Ownership](https://doc.qt.io/qt-6/objecttrees.html)*
>
> 协议：本翻译遵守原文档使用的 [GFDLv1.3](https://www.gnu.org/licenses/fdl-1.3.html) 授权
>
> 译者：[muzing](https://muzing.top/about/)
>
> 翻译时间：2022.06

## 概述

[QObjects](https://doc.qt.io/qt-6/qobject.html) 在对象树（object trees）中组织自身。当创建一个以另一个对象为父对象的 [QObject](https://doc.qt.io/qt-6/qobject.html) 时，它会被添加到父对象的 [children](https://doc.qt.io/qt-6/qobject.html#children)() 列表中，并在父对象被销毁时销毁。事实证明，这种方式非常适合 GUI 对象的需求。例如，一个 [QShortcut](https://doc.qt.io/qt-6/qshortcut.html) （键盘快捷键）是相关窗口的子对象，因此当用户关闭该窗口时，快捷键也会被销毁。

[QQuickItem](https://doc.qt.io/qt-6/qquickitem.html) 是 Qt Quick 模块的基本视觉元素，继承自 [QObject](https://doc.qt.io/qt-6/qobject.html)，但有一个与 *[QObject](https://doc.qt.io/qt-6/qobject.html) 父对象*不同的*视觉父项*的概念。一个项目的视觉父项可能并不是其父对象。参阅 [Concepts - Visual Parent in Qt Quick](https://doc.qt.io/qt-6/qtquick-visualcanvas-visualparent.html) 获取更多详细信息。

[QWidget](https://doc.qt.io/qt-6/qwidget.html)，即 Qt Widgets 模块的基础类，扩展了父子关系。一个普通子对象也成为一个子控件，也就是说，它会被显示在父级的坐标系中，并被其父级的边界按图形方式裁剪。例如，当应用程序在关闭消息框后销毁它时，正如我们所希望的那样，消息框的按钮和标签也被销毁，这是因为按钮和标签是消息框的子控件。

您也可以自行删除子对象，它们会自动从其父控件中移除自己。例如，当用户移除一项工具栏时，可能会导致应用程序删除其 [QToolBar](https://doc.qt.io/qt-6/qtoolbar.html) 对象之一，在这种情况下，工具栏的父对象 [QMainWindow](https://doc.qt.io/qt-6/qmainwindow.html) 将检测到变化，并相应地重新配置其屏幕空间。

当应用程序视觉上或行为上表现异常时，调试函数 [QObject::dumpObjectTree](https://doc.qt.io/qt-6/qobject.html#dumpObjectTree)() 和 [QObject::dumpObjectInfo](https://doc.qt.io/qt-6/qobject.html#dumpObjectInfo)() 通常很有用。

## QObjects 的构造/销毁顺序

当 [QObjects](https://doc.qt.io/qt-6/qobject.html) 在堆上创建（即，使用 *new* 创建）时，可以以任意顺序从它们构建对象树，稍后，可以以任意顺序销毁树中的对象。当任何 [QObjects](https://doc.qt.io/qt-6/qobject.html) 被删除时，如果该对象有父对象，则析构函数会自动从其父对象中删除该对象。如果该对象有子对象，则析构函数会自动删除每个子对象。不管销毁的顺序，没有 [QObjects](https://doc.qt.io/qt-6/qobject.html) 会被删除两次。

当 [QObjects](https://doc.qt.io/qt-6/qobject.html) 在栈上创建时，适用相同的行为。通常，破坏顺序仍不会造成问题。考虑一下代码段：

```c++
int main()
{
    QWidget window;
    QPushButton quit("Quit", &window);
    ...
}
```

父对象 `window` 和子对象 `quit` 都是 [QObjects](https://doc.qt.io/qt-6/qobject.html)，因为 [QPushButton](https://doc.qt.io/qt-6/qpushbutton.html) 继承自 [QWidget](https://doc.qt.io/qt-6/qwidget.html)，[QWidget](https://doc.qt.io/qt-6/qwidget.html) 又继承自 [QObjects](https://doc.qt.io/qt-6/qobject.html)。这段代码是正确的：`quit` 的析构函数*没有*被调用两次，因为 C++ 语言标准 *(ISO/IEC 14882:2003)* 指定本地对象的析构函数按其构造函数的相反顺序调用。因此，先调用子对象 `quit` 的析构函数，然后将自己从其父对象 `window` 中移除，再调用 `window` 的析构函数。

但是考虑一下如果交换构造顺序会发生什么，如第二个片段所示：

```c++
int main()
{
    QPushButton quit("Quit");
    QWidget window;

    quit.setParent(&window);
    ...
}
```

在这种情况下，破坏顺序会引发问题。首先调用父对象的析构函数，因为它是最后被创建的。然后调用其子对象 `quit` 的析构函数，但这是不正确的，因为 `quit` 是一个局部变量。当 `quit` 随后超出作用域时，其析构函数再次被调用，这一次是正确的，但已经发生了破坏。

------

© 2022 The Qt Company Ltd. Documentation contributions included herein are the copyrights of their respective owners. The documentation provided herein is licensed under the terms of the [GNU Free Documentation License version 1.3](https://www.gnu.org/licenses/fdl-1.3.html) as published by the Free Software Foundation. Qt and respective logos are trademarks of The Qt Company Ltd. in Finland and/or other countries worldwide. All other trademarks are property of their respective owners.

© 2022 zh_CN Translation by muzing\<muzi2001@foxmail.com>.
