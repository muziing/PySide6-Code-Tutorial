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
