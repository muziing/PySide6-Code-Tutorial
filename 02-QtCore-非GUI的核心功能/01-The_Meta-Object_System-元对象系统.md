# 元对象系统

> 翻译信息：
>
> 本文翻译自 PySide6 官方文档 *[The Meta-Object System](https://doc.qt.io/qtforpython/overviews/metaobjects.html)*
>
> 协议：本翻译遵守原文档使用的 [GNU Free Documentation License version 1.3](https://www.gnu.org/licenses/fdl-1.3.html) 授权
>
> 译者：[muzing](https://muzing.top/about/)
>
> 翻译时间：2022.06
>
> 译者注：本文原文由 [Qt 6(C++) 文档](https://doc.qt.io/qt-6/metaobjects.html)直接转换而来，似乎代码部分并未完全替换为有效的 Python 代码，建议与 C++ 原版文档对比阅读

Qt 的元对象系统（meta-object system）和自省（introspection）功能的概述。

Qt 的元对象系统为对象间通信、运行时类型信息和动态属性系统提供了信号与槽机制。

元对象系统基于三件事：

1. `QObject` 类为可以利用元对象系统的对象提供基类。
2. 类声明私有部分中的 `Q_OBJECT` 宏用于启用元对象特性，例如动态属性、信号和槽。
3. 元对象编译器 (`moc`) 为每个 `QObject` 子类提供实现元对象功能所需的代码。

`moc` 工具读取 C++ 源文件。如果它找到一个或多个包含 `Q_OBJECT` 宏的类声明，它会生成另一个 C++ 源文件，其中包含每个类的元对象代码。这个生成的源文件要么是 `#include` 被包含在类的源文件中，要么（更常见地）是被编译并与类的实现链接。

除了提供对象间通信的[信号与槽](https://doc.qt.io/qtforpython/overviews/signalsandslots.html#signals-slots)机制（这是引入系统的主要原因），元对象代码还提供以下附加功能：

- `metaObject()` 返回类的关联 `meta-object`
- `className()` 在运行时将类名作为字符串返回，无需通过 C++ 编译器支持本机运行时类型信息（RTTI）
- `inherits()` 函数返回对象是否继承 `QObject` 继承树中指定类的类的实例
- `tr()` 翻译字符以进行国际化
- `setProperty()` 和 `property()` 按名称动态设置和获取属性
- `newInstance()` 构造一个新的类实例

也可以在 `QObject` 类上使用 `qobject_cast()` 执行动态转换。`qobject_cast()` 函数的行为类似于 标准 C++ 的 `dynamic_cast()`，其优点是不需要 RTTI 支持，并且可以跨动态库边界工作。它尝试将其参数转换为尖括号中指定的指针类型，如果对象的类型正确（在运行时确定），则返回非零指针；如果对象的类型不兼容，则返回 `None`。

例如，假设 `MyWidget` 继承自 `QWidget` 并使用 `Q_OBJECT` 宏声明：

```python
obj = MyWidget()
```

`QObject *` 类型的 `obj` 变量实际上是指 `MyWidget` 对象，所以我们可以适当地转换它：

```python
widget = QWidget (obj)
```

成功从 `QObject` 转换到 `QWidget`，因为对象其实是一个 `MyWidget`，它是 `QWidget` 的子类。由于我们知道 `obj` 是一个 `MyWidget`，所以也可以将其转换为 `MyWidget *`：

```python
myWidget = MyWidget (obj)
```

转换至 `MyWidget` 成功，因为 `qobject_cast()` 没有区分内置 Qt 类型和自定义类型。

```python
label = QLabel (obj)
# label is 0
```

另一方面，转换为 `QLabel` 失败。指针然后被设置为 0。这使得可以在运行时根据类型以不同的方式处理不同类型的对象：

```python
if (QLabel label = QLabel (obj)) {            label.setText(tr("Ping"))
} else if (QPushButton button = QPushButton (obj)) {
    button.setText(tr("Pong!"))
```

虽然可以在没有 `Q_OBJECT` 宏和元对象代码的情况下使用 `QObject` 作为基类，但如果不使用 `Q_OBJECT` 宏，则信号和槽、以及此处描述的其他功能都将不可用。从元对象系统的角度来看，没有元代码的 `QObject` 子类等价于最接近的具有元对象代码的祖先 。这意味着，例如，`className()` 不会返回类的实际名称，而是这个祖先的类名。

因此，我们强烈建议 `QObject` 的所有子类都使用 `Q_OBJECT` 宏，无论它们是否真的使用信号、槽和属性。

------

© 2022 The Qt Company Ltd. Documentation contributions included herein are the copyrights of their respective owners. The documentation provided herein is licensed under the terms of the [GNU Free Documentation License version 1.3](https://www.gnu.org/licenses/fdl-1.3.html) as published by the Free Software Foundation. Qt and respective logos are trademarks of The Qt Company Ltd. in Finland and/or other countries worldwide. All other trademarks are property of their respective owners. 

© 2022 zh_CN Translation by muzing\<muzi2001@foxmail.com>.
