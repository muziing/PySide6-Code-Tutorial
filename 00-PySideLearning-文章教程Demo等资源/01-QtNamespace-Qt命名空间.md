# Qt 命名空间

[QtCore.Qt 命名空间](https://doc.qt.io/qt-6/qt.html)下包含了整个 Qt 库中所使用的各种标识符。

这些标识符大多为枚举（enum）或标志（flags）类型。本文收录部分标识符文档的中文翻译，按字母顺序排列。

## A

### [Alignment](https://doc.qt.io/qt-6/qt.html#AlignmentFlag-enum)

Qt.AlignmentFlag 中又分为水平对齐方式与垂直对齐方式，具体有如下数种：

水平对齐：

| 常量              | 值      | 描述                 |
|-----------------|--------|--------------------|
| Qt.AlignLeft    | 0x0001 | 与左边缘对齐             |
| Qt.AlignRight   | 0x0002 | 与右边缘对齐             |
| Qt.AlignHCenter | 0x0004 | 在可用空间中水平居中         |
| Qt.AlignJustify | 0x0008 | 两端对齐（尽可能使文字占满横向空间） |

垂直对齐：

| 常量               | 值      | 描述         |
|------------------|--------|------------|
| Qt.AlignTop      | 0x0020 | 与顶部对齐      |
| Qt.AlignBottom   | 0x0040 | 与底部对齐      |
| Qt.AlignVCenter  | 0x0080 | 在可用空间中垂直居中 |
| Qt.AlignBaseline | 0x0100 | 与基线对齐      |

若需同时设置水平、垂直两个维度的对齐方式，只需将两个Flags用或运算符连接，例如：
`Qt.AlignCenter` 等价于 `Qt.AlignVCenter | Qt.AlignHCenter`

## F

### [FocusPolicy](https://doc.qt.io/qt-6/qt.html#FocusPolicy-enum)

| 常量             | 值             | 描述                               |
|----------------|---------------|----------------------------------|
| Qt.TabFocus    | 0x1           | 通过键盘Tab键获取焦点                     |
| Qt.ClickFocus  | 0x2           | 通过鼠标点击获取焦点                       |
| Qt.StrongFocus | TabFocus \| ClickFocus \| 0x8 | 通过键盘Tab或鼠标点击获取焦点                              |
| Qt.WheelFocus  | StrongFocus \| 0x4                              | 在StrongFocus基础上，还支持鼠标滚轮滚动获取焦点            |
| Qt.NoFocus     | 0             | 该控件不接受焦点，QLabel等不需要用户键盘操作的控件的默认值 |

## S

### [ScrollBarPolicy](https://doc.qt.io/qt-6/qt.html#ScrollBarPolicy-enum)

此枚举类型描述了 [QAbstractScrollArea](https://doc.qt.io/qt-6/qabstractscrollarea.html) 滚动条的各种模式。水平滚动条与垂直滚动条的模式相互独立。

| 常量                  | 值   | 描述                                                         |
| --------------------- | ---- | ------------------------------------------------------------ |
| Qt.ScrollBarAsNeeded  | 0    | 只有当内容太大而无法容纳时，QAbstractScrollArea 才显示滚动条。此为默认值。 |
| Qt.ScrollBarAlwaysOff | 1    | QAbstractScrollArea 永不显示滚动条。                         |
| Qt.ScrollBarAlwaysOn  | 2    | QAbstractScrollArea 总显示一个滚动条。此属性在具有瞬态滚动条的操作系统上被忽略。 |

## T

### [TextElideMode](https://doc.qt.io/qt-6/qt.html#TextElideMode-enum)

此枚举值指定显示需省略的文本时省略号应出现的位置：

| 常量           | 值   | 描述                       |
| -------------- | ---- | -------------------------- |
| Qt.ElideLeft   | 0    | 省略号应出现在文本的开头。 |
| Qt.ElideRight  | 1    | 省略号应出现在文本的末尾。 |
| Qt.ElideMiddle | 2    | 省略号应出现在文本的中间。 |
| Qt.ElideNone   | 3    | 省略号不应出现在文本中。   |

`Qt.ElideMiddle` 通常是最适合 URL 的选择（例如，"http://bugreports.qt.../QTWEBSITE-13/"），而 `Qt.ElideRight` 适合其他字符串。

### [TextFormat](https://doc.qt.io/qt-6/qt.html#TextFormat-enum)

| 常量              | 值   | 描述                     |
|-----------------|-----|------------------------|
| Qt.PlaintText   | 0   | 将文本字符串解析为纯文本           |
| Qt.RichText     | 1   | 将文本字符串解析为富文本           |
| Qt.AutoText     | 2   | 自动识别为纯文本或富文本           |
| Qt.MarkdownText | 3   | 将文本字符串解析为Markdown格式的文本 |

### [TextInteractionFlag](https://doc.qt.io/qt-6/qt.html#TextFormat-enum)

| 常量                           | 值                       | 描述                               |
|------------------------------|-------------------------|----------------------------------|
| Qt.NoTextInteraction         | 0                       | 不能与文本进行交互                        |
| Qt.TextSelectableByMouse     | 1                       | 可以使用鼠标选择文本，并用上下文菜单或标准键盘快捷键复制到剪贴板 |
| Qt.TextSelectableByKeyboard  | 2                       | 可以用键盘上的光标键选择文本，会显示一个文本光标         |
| Qt.LinksAccessibleByMouse    | 4                       | 链接高亮显示，并可用鼠标激活                   |
| Qt.LinksAccessibleByKeyboard | 8                       | 链接可以使用Tab键获得焦点，并通过Enter键激活       |
| Qt.TextEditable              | 16                      | 文本完全可编辑                          |
| Qt.TextEditorInteraction     | TextSelectableByMouse \| TextSelectableByKeyboard \| TextEditable | 文本编辑器的默认值                                           |
| Qt.TextBrowserInteraction    | TextSelectableByMouse \| LinksAccessibleByMouse \| LinksAccessibleByKeyboard | QTextBrowser的默认值                                         |
