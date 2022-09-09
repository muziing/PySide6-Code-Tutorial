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

## C

### [CursorMoveStyle](https://doc.qt.io/qt-6/qt.html#CursorMoveStyle-enum)

此枚举值描述文本光标移动的风格。逻辑风格中，键盘左箭头意味着光标向文本的前方移动（对于从右至左的文本，前方意味着右方）；而视觉风格中，键盘左箭头意味着光标向视觉上的左侧移动，而不考虑文本书写方向。

| 常量                | 值   | 描述                                                         |
| ------------------- | ---- | ------------------------------------------------------------ |
| Qt.LogicalMoveStyle | 0    | 在从左至右的文本块内，按下键盘左方向键时减少光标位置，右方向键增加光标位置；在从右向左的文本块内相反。 |
| Qt.VisualMoveStyle  | 1    | 无论书写方向如何，按下键盘左方向键光标总会向左移动，按下右方向键光标向右移动。 |

## F

### [FocusPolicy](https://doc.qt.io/qt-6/qt.html#FocusPolicy-enum)

| 常量             | 值             | 描述                               |
|----------------|---------------|----------------------------------|
| Qt.TabFocus    | 0x1           | 通过键盘Tab键获取焦点                     |
| Qt.ClickFocus  | 0x2           | 通过鼠标点击获取焦点                       |
| Qt.StrongFocus | TabFocus \| ClickFocus \| 0x8 | 通过键盘Tab或鼠标点击获取焦点                              |
| Qt.WheelFocus  | StrongFocus \| 0x4                              | 在StrongFocus基础上，还支持鼠标滚轮滚动获取焦点            |
| Qt.NoFocus     | 0             | 该控件不接受焦点，QLabel等不需要用户键盘操作的控件的默认值 |

## L

### [LayoutDirection](https://doc.qt.io/qt-6/qt.html#LayoutDirection-enum)

控制 Qt 的布局与文字方向。

| 常量                   | 值   | 描述         |
| ---------------------- | ---- | ------------ |
| Qt.LeftToRight         | 0    | 从左至右布局 |
| Qt.RightToLeft         | 1    | 从右至左布局 |
| Qt.LayoutDirectionAuto | 2    | 自动布局     |

对于阿拉伯语、希伯来语等特定语言，需要从右至左布局。

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

## W

### [WindowModality](https://doc.qt.io/qt-6/qt.html#WindowModality-enum)

此枚举值用于控制窗口的模态行为。对话框窗口大多为模态窗口。

| 常量                | 值   | 描述                                                         |
| ------------------- | ---- | ------------------------------------------------------------ |
| Qt.NonModal         | 0    | 窗口为非模态，不阻塞其他窗口的输入                           |
| Qt.WindowModal      | 1    | 窗口对单个窗口结构层次为模态，阻塞对其父窗口（及其的兄弟窗口）、祖父窗口（及其兄弟窗口）的输入 |
| Qt.ApplicationModal | 2    | 窗口对应用程序为模态，阻塞对所有窗口的输入                   |

### [WindowType](https://doc.qt.io/qt-6/qt.html#WindowType-enum)

此枚举值用于为控件指定各种窗口系统（window-system）属性。它们一般比较少见，但在少数情况下是必要的。其中一些标志取决于底层窗口管理器是否支持。

主要类型包括：

| 常量             | 值                   | 描述                                                         |
| ---------------- | -------------------- | ------------------------------------------------------------ |
| Qt.Widget        | 0x00000000           | [QWidget](https://doc.qt.io/qt-6/qwidget.html) 的默认类型。这种类型的控件如果有父控件则作为子控件，若没有父控件则为独立窗口。参见 Qt.Window 和 Qt.SubWindow。 |
| Qt.Window        | 0x00000001           | 表示该控件是一个窗口，不管该控件是否有父控件，一般带有一个窗口系统框架和一个标题栏。注意如果控件没有父对象，则无法取消设置此标志。 |
| Qt.Dialog        | 0x00000002 \| Window | 表示该控件是一个应装饰为对话框的窗口（即，一般在标题栏中没有最大化最小化按钮）。这是 [QDialog](https://doc.qt.io/qt-6/qdialog.html) 的默认类型。如果想用它作为模态对话框，它应该从另一个窗口启动，或者有父窗口并与 [QWidget.windowModality](https://doc.qt.io/qt-6/qwidget.html#windowModality-prop) 属性一起使用。如果将其设置为模态，对话框将阻止应用程序中的其他顶级窗口获得任何输入。我们将具有父控件的顶级窗口称为次要窗口（secondary window）。 |
| Qt.Sheet         | 0x00000004 \| Window | 表示窗口是 macOS 上的 sheet。由于使用 sheet 意味着窗口模式，因此推荐的方法是使用 [QWidget.setWindowModality](https://doc.qt.io/qt-6/qwidget.html#windowModality-prop)() 或 [QDialog::open](https://doc.qt.io/qt-6/qdialog.html#open)() 替代。 |
| Qt.Popup         | 0x00000008 \| Window | 表示该控件是一个弹出式顶级窗口，即它是模态的，但具有适合弹出式菜单的窗口系统框架。 |
| Qt.Tool          | Popup \| Dialog      | 表示该控件是一个工具窗口。工具窗口通常是一个小窗口，具有比一般窗口更小的标题栏和装饰，一般用于工具按钮的集合。如果有父控件，则工具窗口将始终保留在其顶部。如果没有父级，也可以考虑使用 Qt::WindowStaysOnTopHint。如果窗口系统支持，工具窗口可以用更轻量的框架来装饰。它也可以与 Qt::FramelessWindowHint 结合使用。在 macOS 上，工具窗口对应于窗口的 [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) 类。这意味着窗口位于普通窗口之上，因此无法在其上层放置普通窗口。默认情况下，当应用程序处于非活动状态时，工具窗口将消失。这可以通过 [Qt.WA_MacAlwaysShowToolWindow](https://doc.qt.io/qt-6/qt.html#WidgetAttribute-enum) 属性来控制。 |
| Qt.ToolTip       | Popup \| Sheet       | 表明该控件是工具提示。这在内部用于实现工具提示。             |
| Qt.SplashScreen  | ToolTip \| Dialog    | 表明该窗口是闪屏（splash screen）。这是 [QSplashScreen](https://doc.qt.io/qt-6/qsplashscreen.html) 的默认类型。 |
| Qt.SubWindow     | 0x00000012           | 表明此控件是子窗口，例如 [QMdiSubWindow](https://doc.qt.io/qt-6/qmdisubwindow.html) 控件。 |
| Qt.ForeignWindow | 0x00000020 \| Window | 表明此窗口对象是一个句柄，表示由另一个进程或手动使用本地代码创建的本地平台窗口。 |
| Qt.CoverWindow   | 0x00000040 \| Window | 表示该窗口代表一个覆盖窗口，在某些平台上最小化应用程序时显示。 |

还有许多标志可用于自定义顶级窗口的外观。这对其他窗口没有影响：

| 常量                                   | 值                                                   | 描述                                                         |
| -------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| Qt.MSWindowsFixedSizeDialogHint        | 0x00000100                                           | 在微软 Windows 上为窗口提供一个细对话框边框。这种风格传统上用于固定大小的对话框。注意：不建议在多显示器环境中使用此标志，因为系统将强制窗口在跨屏幕移动时保持其原始大小，这在使用具有不同分辨率的显示器时尤其不受欢迎。 |
| Qt.MSWindowsOwnDC                      | 0x00000200                                           | 在微软 Windows 上为窗口提供自己的显示上下文。                |
| Qt.BypassWindowManagerHint             | 0x00000400                                           | 此标志可用于向平台插件指示应禁用“所有”窗口管理器协议。根据应用程序运行的操作系统和窗口管理器运行的情况，该标志的行为会有所不同。该标志可用于获取未设置配置的本机窗口。 |
| Qt.X11BypassWindowManagerHint          | BypassWindowManagerHint                              | 完全绕过窗口管理器。这会导致一个完全不受管理的无边框窗口（即，除非手动调用 [QWidget.activateWindow](https://doc.qt.io/qt-6/qwidget.html#activateWindow)()，否则没有键盘输入）。 |
| Qt.FramelessWindowHint                 | 0x00000800                                           | 生成无边框窗口。用户不能通过窗口系统移动或调整无边框窗口的大小。在 X11 上，标志的结果取决于窗口管理器及其理解 Motif 和/或 NETWM 的能力。大多数现有的现代窗口管理器都可以处理这个问题。 |
| Qt.NoDropShadowWindowHint              | 0x40000000                                           | 禁用在支持的平台上的窗口投影。                               |
| Qt.CustomizeWindowHint                 | 0x02000000                                           | 关闭默认窗口标题 hints。                                     |
| Qt.WindowTitleHint                     | 0x00001000                                           | 为窗口添加标题栏。                                           |
| Qt.WindowSystemMenuHint                | 0x00002000                                           | 为窗口添加系统菜单，很可能是一个关闭按钮。如果想要隐藏/显示关闭按钮，更好的做法是使用 WindowCloseButtonHint。 |
| Qt.WindowMinimizeButtonHint            | 0x00004000                                           | 为窗口添加最小化按钮。在某些平台上，这意味着 WindowSystemMenuHint 也已生效。 |
| Qt.WindowMaximizeButtonHint            | 0x00008000                                           | 为窗口添加最大化按钮。在某些平台上，这意味着 WindowSystemMenuHint 也已生效。 |
| Qt.WindowMinMaxButtonsHint             | WindowMinimizeButtonHint \| WindowMaximizeButtonHint | 为窗口添加最大化、最小化按钮。在某些平台上，这意味着 WindowSystemMenuHint 也已生效。 |
| Qt.WindowCloseButtonHint               | 0x08000000                                           | 为窗口添加关闭按钮。在某些平台上，这意味着 WindowSystemMenuHint 也已生效。 |
| Qt.WindowContextHelpButtonHint         | 0x00010000                                           | 为对话框添加上下文帮助按钮。在某些平台上，这意味着 WindowSystemMenuHint 也已生效。 |
| Qt.MacWindowToolBarButtonHint          | 0x10000000                                           | 在 macOS 上添加一个工具栏按钮（即，在有工具栏的窗口的右上方的椭圆形按钮） |
| Qt.WindowFullscreenButtonHint          | 0x80000000                                           | 在 macOS 上添加一个全屏按钮                                  |
| Qt.BypassGraphicsProxyWidget           | 0x20000000                                           | 如果父控件已经嵌入，则阻止窗口及其子窗口自动将自己嵌入到 QGraphicsProxyWidget 中。如果希望控件始终是桌面上的顶级控件，则可以设置此标志，无论父控件是否已嵌入场景中。 |
| Qt.WindowShadeButtonHint               | 0x00020000                                           | 如果底层窗口管理器支持，则添加一个阴影按钮替代最小化按钮。   |
| Qt.WindowStaysOnTopHint                | 0x00040000                                           | 通知窗口系统该窗口应位于所有其他窗口之上。注意，在某些基于 X11 的窗口管理器上，还必须传递 Qt.X11BypassWindowManagerHint 才能使此标志正常工作。 |
| Qt.WindowStaysOnBottomHint             | 0x04000000                                           | 通知窗口系统该窗口应位于所有其他窗口之下。                   |
| Qt.WindowTransparentForInput           | 0x00080000                                           | 通知窗口系统该窗口仅用于输出（显示某些内容）而不接受输入。因此输入事件应该像不存在一样略过。 |
| Qt.WindowOverridesSystemGestures       | 0x00100000                                           | 通知窗口系统该窗口实现了自己的一组手势，系统级的手势（例如三指切换屏幕）应当被禁用。 |
| Qt.WindowDoesNotAcceptFocus            | 0x00200000                                           | 通知窗口系统该窗口不接受输入焦点。                           |
| Qt.MaximizeUsingFullscreenGeometryHint | 0x00400000                                           | 通知窗口系统在最大化窗口时应尽可能多地使用可用的屏幕几何空间，包括可能被UI覆盖的区域（例如状态栏或应用程序启动器）。这可能会导致窗口被置于这些系统UI之下，具体情况取决于平台是否支持。启用该标志后，用户负责将 [QScreen.availableGeometry](https://doc.qt.io/qt-6/qscreen.html#availableGeometry-prop)() 也考虑在内，以便应用程序中需要用户交互的任何UI元素都不会被系统UI覆盖。 |
| Qt.WindowType_Mask                     | 0x000000ff                                           | 用于从窗口标志中提取窗口类型的掩码。                         |
