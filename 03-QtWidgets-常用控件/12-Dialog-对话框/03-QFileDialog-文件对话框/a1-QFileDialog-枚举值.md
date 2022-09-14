# QFileDialog-枚举值

由于 [QFileDialog](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFileDialog.html) 类中包含大量的枚举值类型，故单独摘录整理至本文档中。

## [AcceptMode](https://doc.qt.io/qt-6/qfiledialog.html#AcceptMode-enum)

| 常量       | 值   |
| ---------- | ---- |
| AcceptOpen | 0    |
| AcceptSave | 1    |

## [DialogLabel](https://doc.qt.io/qt-6/qfiledialog.html#DialogLabel-enum)

| 常量     | 值   |
| -------- | ---- |
| LookIn   | 0    |
| FileName | 1    |
| FileType | 2    |
| Accept   | 3    |
| Reject   | 4    |

## [FileMode](https://doc.qt.io/qt-6/qfiledialog.html#FileMode-enum)

此枚举值用于指示用户可以在文件对话框中选择什么；即，如果用户单击确定，对话框将返回什么。

| 常量          | 值   | 描述                                                         |
| ------------- | ---- | ------------------------------------------------------------ |
| AnyFile       | 0    | 单一的、现有的或不存在的文件的文件名                         |
| ExistingFile  | 1    | 单一的、现有的文件的文件名                                   |
| Directory     | 2    | 一个目录的名称。文件和目录都会显示。注意原生Windows文件对话框不支持在目录选择器中显示文件 |
| ExistingFiles | 3    | 零个或多个现有文件的名称                                     |

## [Option](https://doc.qt.io/qt-6/qfiledialog.html#Option-enum)

| 常量                        | 值         | 描述                                                         |
| --------------------------- | ---------- | ------------------------------------------------------------ |
| ShowDirsOnly                | 0x00000001 | 在文件对话框中仅显示目录。默认情况下文件和目录都会显示。（仅在目录文件模式下有效。） |
| DontResolveSymlinks         | 0x00000002 | 不要在文件对话框中解析符号链接。默认情况下会解析符号链接。   |
| DontConfirmOverwrite        | 0x00000004 | 如果选择了一个现有文件，则不请求确认。默认情况下会要求确认。 |
| DontUseNativeDialog         | 0x00000008 | 不要使用原生文件对话框。默认情况下会使用原生对话框，除非使用包含 [Q_OBJECT](https://doc.qt.io/qt-6/qobject.html#Q_OBJECT) 宏的 QFileDialog 的子类，或平台没有您需要的类型的本地对话框。注意在使用原生文件对话框时，此选项在 MacOS 上不支持。 |
| ReadOnly                    | 0x00000010 | 声明模型是只读的。必须在更改对话框属性或显示对话框之前设置此选项。 |
| HideNameFilterDetails       | 0x00000020 | 声明文件名过滤器详细信息是否隐藏。                           |
| DontUseCustomDirectoryIcons | 0x00000040 | 始终使用默认目录图标。某些平台支持用户设置不同的图标，但自定义图标查找会对网络或可移动驱动器造成很大的性能影响。设置此选项将启用图标提供器中的 QFileIconProvider.DontUseCustomDirectoryIcons 选项。 |

## [ViewMode](https://doc.qt.io/qt-6/qfiledialog.html#ViewMode-enum)

此枚举值描述了文件对话框的视图模式，即，将显示关于每个文件的哪些信息

| 常量   | 值   | 描述                                 |
| ------ | ---- | ------------------------------------ |
| Detail | 0    | 为目录中的每一项显示图标、名称、详情 |
| List   | 1    | 为目录中的每一项只显示图标和名称     |
