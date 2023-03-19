"""
QLineEdit 编辑操作

QLineEdit 提供了一批用于编辑操作的槽函数

============================= 槽函数 =================================

.clear()               清除单行编辑器的内容
.copy()                将选中的文本复制到剪切板，前提是EchoMode为Normal
.cut()                 将选中的文本复制到剪切板并从编辑器中删除，前提是EchoModeNormal
.paste()               将剪切板中的文字插入到当前光标位置，删除所有选中的文字，前提是编辑器不处于只读模式
.undo()                撤销最后一步操作，前提是撤销可用
.redo()                重做最后一次操作，前提是重做可用
.selectAll()           选择所有的文字并将光标移至末尾
.setText(text: str)    设置文本

============================= 其他 ======================================

.home(mark: bool)      将光标移动到行首
.end(mark: bool)       将光标移动至行尾
对于home/end，如果maek为True，则将一直向前选中到首位置；否则任何已经选中的文本将在光标移动时取消选中

.del_()                若未选中文本，则删除光标右侧的字符；若选中了文本，则光标移至选中起始位置并删除选中文本
.backspace()           若未选中文本，则删除光标左侧的字符；若选中了文本，则光标移至选中起始位置并删除选中文本

获取撤销/重做的可用状态
.isRedoAvailable() -> bool              获取当前是否可以撤销，默认为False（因为用户还未进行任何操作）
.isUndoAvailable() -> bool              获取当前是否可以重做

是否允许拖拽，用户可以选中部分文本进行拖拽，甚至可以拖拽到另一个编辑器中
.setDragEnabled(b: bool)                设置是否允许拖拽，默认不允许
.dragEnabled() -> bool                  获取拖拽允许状态

在编辑器内添加一个清空按钮，当编辑器内容不为空时显示在末尾
.setClearButtonEnabled(enable: bool)    在编辑器内添加清空按钮
.isClearButtonEnabled() -> bool         是否启用了清空按钮

当用户对单行编辑器的内容有修改后，Modified属性会从默认的False变成True
.setModified(yes: bool)                 手动设置Modified状态
.isModified() -> bool                   获取用户是否对编辑器有修改
"""

import sys

from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-编辑操作")
        self.resize(600, 400)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""

        self.line_edit_1 = QtWidgets.QLineEdit()
        self.line_edit_2 = QtWidgets.QLineEdit()
        self.line_edit_1.setPlaceholderText("主要测试编辑器")
        self.line_edit_2.setPlaceholderText("辅助测试编辑器")

        self.clear_button = QtWidgets.QPushButton("清空")
        self.select_all_button = QtWidgets.QPushButton("全选")
        self.copy_button = QtWidgets.QPushButton("复制")
        self.cut_button = QtWidgets.QPushButton("剪切")
        self.paste_button = QtWidgets.QPushButton("粘贴")
        self.undo_button = QtWidgets.QPushButton("撤销")
        self.redo_button = QtWidgets.QPushButton("重做")
        self.home_end_button = QtWidgets.QPushButton("Home/End")
        self.backspace_del_button = QtWidgets.QPushButton("Backspace/Del")

        # 使用布局管理器布局控件
        # 首次学习时可以略过本段代码
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.clear_button)
        layout.addWidget(self.select_all_button)
        layout.addWidget(self.cut_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.paste_button)
        layout.addWidget(self.undo_button)
        layout.addWidget(self.redo_button)
        layout.addWidget(self.home_end_button)
        layout.addWidget(self.backspace_del_button)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.line_edit_1)
        main_layout.addWidget(self.line_edit_2)
        main_layout.addLayout(layout)

        self.setLayout(main_layout)

    def test_01(self) -> None:
        """测试槽函数"""

        self.clear_button.clicked.connect(self.line_edit_1.clear)  # type: ignore
        self.select_all_button.clicked.connect(self.line_edit_1.selectAll)  # type: ignore
        self.cut_button.clicked.connect(self.line_edit_1.cut)  # type: ignore
        self.copy_button.clicked.connect(self.line_edit_1.copy)  # type: ignore
        self.paste_button.clicked.connect(self.line_edit_1.paste)  # type: ignore
        self.undo_button.clicked.connect(self.line_edit_1.undo)  # type: ignore
        self.redo_button.clicked.connect(self.line_edit_1.redo)  # type: ignore
        # 当编辑器1的文本改变时，将其文本设置给编辑器2
        self.line_edit_1.textChanged.connect(self.line_edit_2.setText)  # type: ignore

    def test_02(self) -> None:
        """测试其他编辑功能"""

        @QtCore.Slot()
        def test_home_end():
            # 以下四行测试时打开一行，注释掉其他三行
            self.line_edit_1.home(False)
            # self.line_edit_1.home(True)
            # self.line_edit_1.end(False)
            # self.line_edit_1.end(True)
            self.line_edit_1.setFocus()  # 令单行编辑器重新获得焦点

        @QtCore.Slot()
        def test_backspace_del():
            self.line_edit_1.backspace()
            # self.line_edit_1.del_()
            self.line_edit_1.setFocus()  # 令单行编辑器重新获得焦点

        # 测试编辑键
        self.home_end_button.clicked.connect(test_home_end)  # type: ignore
        self.backspace_del_button.clicked.connect(test_backspace_del)  # type: ignore

        # 启用清空按钮：当编辑器内不为空时，会在最末尾显示一个清空按钮
        self.line_edit_1.setClearButtonEnabled(True)

        # 启用拖拽
        # 可以选中部分文本在同一编辑器中拖拽，也可以拖拽到另一个编辑器中
        self.line_edit_1.setDragEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
