# QMessageBox-枚举值

由于 [QMessageBox](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html) 类中包含大量的枚举值类型，故单独摘录整理至本文档中。

## [ButtonRole](https://doc.qt.io/qt-6/qmessagebox.html#ButtonRole-enum)

| 常量            | 值   | 描述                                                         |
| --------------- | ---- | ------------------------------------------------------------ |
| InvalidRole     | -1   | 该按钮无效                                                   |
| AcceptRole      | 0    | 按下该按钮表示对话被接受（例如 `OK`）                        |
| RejectRole      | 1    | 按下按钮表示对话被拒绝（例如 `Cancel`）                      |
| DestructiveRole | 2    | 按下此按钮会导致破坏性更改（例如「放弃所有更改」）并关闭对话框 |
| ActionRole      | 3    | 单击此按钮会导致对话框中的元素发生变化                       |
| HelpRole        | 4    | 按下此按钮以请求帮助                                         |
| YesRole         | 5    | 按钮类似于 "Yes"                                             |
| NoRole          | 6    | 按钮类似于 "No"                                              |
| ResetRole       | 7    | 该按钮将对话框的字段重置为默认值                             |
| ApplyRole       | 8    | 该按钮应用当前更改                                           |

## [Icon](https://doc.qt.io/qt-6/qmessagebox.html#Icon-enum)

| 常量        | 值   | 描述                           |
| ----------- | ---- | ------------------------------ |
| NoIcon      | 0    | 消息提示框没有任何图标         |
| Information | 1    | 表示普通消息（没有异常）的图标 |
| Warning     | 2    | 表示警告的图标                 |
| Critical    | 3    | 表示严重问题的图标             |
| Question    | 4    | 表示询问的图标                 |

## [StandardButton](https://doc.qt.io/qt-6/qmessagebox.html#StandardButton-enum)

| 常量            | 值         | 描述                             | 按钮角色        |
| --------------- | ---------- | -------------------------------- | --------------- |
| Ok              | 0x00000400 | "OK" 按钮                        | AcceptRole      |
| Open            | 0x00002000 | “打开”按钮                       | AcceptRole      |
| Save            | 0x00000800 | “保存”按钮                       | AcceptRole      |
| Cancel          | 0x00400000 | “取消”按钮                       | RejectRole      |
| Close           | 0x00200000 | “关闭”按钮                       | RejectRole      |
| Discard         | 0x00800000 | “放弃”或“不保存”按钮，取决于平台 | DestructiveRole |
| Apply           | 0x02000000 | “应用”按钮                       | ApplyRole       |
| Reset           | 0x04000000 | “重置”按钮                       | ResetRole       |
| RestoreDefaults | 0x08000000 | “恢复默认值”按钮                 | ResetRole       |
| Help            | 0x01000000 | “帮助”按钮                       | HelpRole        |
| SaveAll         | 0x00001000 | “保存全部”按钮                   | AcceptRole      |
| Yes             | 0x00004000 | “是”按钮                         | YesRole         |
| YesToAll        | 0x00008000 | “全部选是”按钮                   | YesRole         |
| No              | 0x00010000 | “否”按钮                         | NoRole          |
| NoToAll         | 0x00020000 | “全部选否”按钮                   | NoRole          |
| Abort           | 0x00040000 | “中止”按钮                       | RejectRole      |
| Retry           | 0x00080000 | “重试”按钮                       | AcceptRole      |
| Ignore          | 0x00100000 | “忽略”按钮                       | AcceptRole      |
| NoButton        | 0x00000000 | 无效的按钮                       | -               |
