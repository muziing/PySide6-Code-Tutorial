# 对象模型

> **翻译信息**：
>
> 本文翻译自 Qt6 官方文档 *[Object Model](https://doc.qt.io/qt-6/object.html)*
>
> 协议：本翻译遵守原文档使用的 [GFDLv1.3](https://www.gnu.org/licenses/fdl-1.3.html) 授权
>
> 译者：[muzing](https://muzing.top/about/)
>
> 翻译时间：2022.06

标准 C++ 对象模型为对象范例提供了非常有效的运行时支持。但它的静态性质在某些具体问题领域不够灵活。GUI 编程是一个需要运行时效率和高灵活性的领域。Qt 通过将 C++ 的速度与 Qt 对象模型的灵活性相结合，来实现这一点。

Qt 为 C++ 添加了如下特性：

- 一种非常强大的无缝对象通信机制，称为[信号与槽](https://doc.qt.io/qt-6/signalsandslots.html)
- 可查询和可设计的[对象属性](https://doc.qt.io/qt-6/properties.html)
- 强大的[事件与事件过滤器](https://doc.qt.io/qt-6/eventsandfilters.html)
- 上下文相关的[用于国际化的字符串翻译](https://doc.qt.io/qt-6/internationalization.html)
- 精巧的间隔驱动[计时器](https://doc.qt.io/qt-6/timers.html)，可以在事件驱动的 GUI 中优雅地集成许多任务
- 以自然方式组织对象所有权的，分层和可查询的[对象树](https://doc.qt.io/qt-6/objecttrees.html)
- 受保护的指针（[QPointer](https://doc.qt.io/qt-6/qpointer.html)）在被引用的对象被销毁时自动设置为 0。这与普通的 C++ 指针不同，后者在其对象被销毁时变成空指针
- 跨库边界工作的[动态转换](https://doc.qt.io/qt-6/metaobjects.html#qobjectcast)
- 支持创建[自定义类型](https://doc.qt.io/qt-6/custom-types.html)

这些 Qt 特性中的许多是基于从 [QObject](https://doc.qt.io/qt-6/qobject.html) 的继承，用标准 C++ 技术实现。其他的，比如对象通信机制和动态属性系统，需要由 Qt 自带的[元对象编译器（moc）](https://doc.qt.io/qt-6/moc.html)提供的[元对象系统](https://doc.qt.io/qt-6/metaobjects.html)。

元对象系统是一种 C++ 扩展，使得该语言更适合真正的组件 GUI 编程。

## 重要的类

这些类构成了 Qt 对象模型的基础。

| [QMetaClassInfo](https://doc.qt.io/qt-6/qmetaclassinfo.html)               | 关于类的附加信息                            |
|----------------------------------------------------------------------------|-------------------------------------|
| [QMetaEnum](https://doc.qt.io/qt-6/qmetaenum.html)                         | 关于枚举器的元数据                           |
| [QMetaMethod](https://doc.qt.io/qt-6/qmetamethod.html)                     | 关于成员函数的元数据                          |
| [QMetaObject](https://doc.qt.io/qt-6/qmetaobject.html)                     | 包含有关 Qt 对象的元信息                      |
| [QMetaProperty](https://doc.qt.io/qt-6/qmetaproperty.html)                 | 关于属性的元数据                            |
| [QMetaSequence](https://doc.qt.io/qt-6/qmetasequence.html)                 | 允许对顺序容器进行类型擦除访问                     |
| [QMetaType](https://doc.qt.io/qt-6/qmetatype.html)                         | 管理元对象系统中的具名类型                       |
| [QObject](https://doc.qt.io/qt-6/qobject.html)                             | 所有 Qt 对象的基类                         |
| [QObjectCleanupHandler](https://doc.qt.io/qt-6/qobjectcleanuphandler.html) | 监视多个 QObject 的生命周期                  |
| [QPointer](https://doc.qt.io/qt-6/qpointer.html)                           | 模板类，提供受保护的指向 QObject 的指针            |
| [QSignalBlocker](https://doc.qt.io/qt-6/qsignalblocker.html)               | 包裹 QObject::blockSignals() 的异常安全包装器 |
| [QSignalMapper](https://doc.qt.io/qt-6/qsignalmapper.html)                 | 绑定来自可识别发送者的信号                       |
| [QVariant](https://doc.qt.io/qt-6/qvariant.html)                           | 行为类似于最常见的 Qt 数据类型的集合                |

## Qt 对象：身份？值？

上面列出的 Qt 对象模型的一些附加功能要求我们将 Qt 对象视为身份（identities），而不是值（values）。值被复制或分配，身份被克隆。克隆意味着创建一个新的身份，而不是旧身份的精确复制品。例如，双胞胎有不同的身份。他们可能看起来相同，但名称不同、位置不同，并且可能有完全不同的社交圈子。

克隆身份是比复制或分配更复杂的操作。我们可以在 Qt 对象模型中看到这意味着什么。

**一个 Qt 对象**……

- 可能有一个唯一的 [QObject::objectName](https://doc.qt.io/qt-6/qobject.html#objectName-prop)()。如果我们复制一个 Qt 对象，该给这个副本起什么名字呢？
- 在[对象层次结构](https://doc.qt.io/qt-6/objecttrees.html)中占据一个位置。如果我们复制一个 Qt 对象，副本应该放在哪里？
- 可以连接到其他 Qt 对象以向它们发出信号或接收它们发出的信号。如果我们复制一个 Qt 对象，该如何将这些连接转移到副本中呢？
- 可以在运行时添加未在 C++ 类中声明的[新属性](https://doc.qt.io/qt-6/properties.html)。如果我们复制一个 Qt 对象，副本是否应该包括添加到原始对象的属性？

出于这些原因，Qt 对象应该被视为身份而不是值。身份是克隆的，而不是复制或分配的，克隆身份是比复制或分配值更复杂的操作。因此，[QObject](https://doc.qt.io/qt-6/qobject.html) 及其所有直接或间接继承的子类，都被禁用了[复制构造函数和赋值运算符](https://doc.qt.io/qt-6/qobject.html#no-copy-constructor)。

------

© 2022 The Qt Company Ltd. Documentation contributions included herein are the copyrights of their respective owners. The documentation provided herein is licensed under the terms of the [GNU Free Documentation License version 1.3](https://www.gnu.org/licenses/fdl-1.3.html) as published by the Free Software Foundation. Qt and respective logos are trademarks of The Qt Company Ltd. in Finland and/or other countries worldwide. All other trademarks are property of their respective owners.

© 2022 zh_CN Translation by muzing\<muzi2001@foxmail.com>.
