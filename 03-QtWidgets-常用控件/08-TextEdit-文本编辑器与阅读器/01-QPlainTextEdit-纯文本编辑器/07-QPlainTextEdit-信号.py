"""
QPlainTextEdit 信号
纯文本编辑器提供了许多可用信号

.textChanged()                            当文档的内容发生变化时发射此信号。例如文本插入删除或应用格式等
.selectionChanged()                       当选中改变时发射此信号
.blockCountChanged(new_block_count: int)  当文档中块的数量发生变化时发射此信号，新的块数量作为参数传出
.cursorPositionChanged()                  当光标位置改变时发射此信号
.copyAvailable(yes: bool)                 当复制功能可用状态发生变化时发射此信号，可用状态作为参数传出
.undoAvailable(available: bool)           当撤销功能可用状态发生变化时发射此信号，可用状态作为参数传出
.redoAvailable(available: bool)           当重做功能可用状态发生变化时发射此信号，可用状态作为参数传出
.updateRequest(rect: QRect, dy: int)      当文本文档需要更新指定的矩形时发射此信号。详情见下一节的案例
.modificationChanged(changed: bool)       当文档的内容以影响修改状态的方式发生变化时发射此信号，文档是否已被修改作为参数传出
"""

import sys

from PySide6 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPlainTextEdit-信号")
        self.resize(800, 600)
        self.pte = QtWidgets.QPlainTextEdit()
        self.info_label = QtWidgets.QLabel()
        self.setup_ui()
        self.signal_test()

    def setup_ui(self) -> None:
        """设置界面"""

        self.pte.resize(600, 450)

        clear_button = QtWidgets.QPushButton("清空")
        copy_button = QtWidgets.QPushButton("复制")
        undo_button = QtWidgets.QPushButton("撤销")
        redo_button = QtWidgets.QPushButton("重做")
        undo_redo_enable_checkbox = QtWidgets.QCheckBox("允许撤销/重做")
        undo_redo_enable_checkbox.setChecked(True)

        @QtCore.Slot(bool)
        def undo_redo_enable_test(enable: bool):
            """测试禁用撤销/重做功能"""
            self.pte.setUndoRedoEnabled(enable)
            print(f"pte.isUndoRedoEnabled({self.pte.isUndoRedoEnabled()})")

        undo_redo_enable_checkbox.toggled.connect(undo_redo_enable_test)  # type: ignore
        clear_button.clicked.connect(self.pte.clear)  # type: ignore
        copy_button.clicked.connect(self.pte.copy)  # type: ignore
        undo_button.clicked.connect(self.pte.undo)  # type: ignore
        redo_button.clicked.connect(self.pte.redo)  # type: ignore

        # 将按钮通过布局管理器放在组框中，首次学习可忽略本段代码
        button_groupbox = QtWidgets.QGroupBox()
        layout = QtWidgets.QVBoxLayout(button_groupbox)
        layout.addWidget(clear_button)
        layout.addWidget(copy_button)
        layout.addWidget(undo_redo_enable_checkbox)
        layout.addWidget(undo_button)
        layout.addWidget(redo_button)
        layout.addWidget(self.info_label)
        button_groupbox.setLayout(layout)

        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(self.pte)
        main_layout.addWidget(button_groupbox)
        self.setLayout(main_layout)

    def signal_test(self) -> None:
        # 测试信号时为避免干扰，每次只测试一个，注释掉其他
        self.pte.textChanged.connect(lambda: self.info_label.setText("文本改变了！"))  # type: ignore
        # self.pte.selectionChanged.connect(lambda: self.info_label.setText("选中内容改变了！"))  # type: ignore
        # self.pte.blockCountChanged.connect(
        #     lambda new_block_count: self.info_label.setText(f"块数量变成了{new_block_count}")
        # )  # type: ignore
        # self.pte.cursorPositionChanged.connect(lambda: self.info_label.setText("光标位置改变了！"))  # type: ignore
        # self.pte.copyAvailable.connect(lambda yes: self.info_label.setText(f"复制可用状态变为了{yes}！"))  # type: ignore
        # self.pte.undoAvailable.connect(lambda yes: self.info_label.setText(f"撤销可用状态变为了{yes}！"))  # type: ignore
        # self.pte.redoAvailable.connect(lambda yes: self.info_label.setText(f"重做可用状态变为了{yes}！"))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
