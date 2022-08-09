import sys

from PySide6 import QtGui, QtWidgets

"""
QLineEdit 信号

由于QLineEdit的信号解释较为复杂，建议参考官方文档的详细信息
https://doc.qt.io/qt-6/qlineedit.html#signals

.textChanged(text: str)    当编辑器中的文本发生改变时发射此信号，新的文本作为参数传出
.textEdited(text: str)     当编辑器中的文本被用户编辑时发射此信号，新的文本作为参数传出，编程方式改变文本无效
.cursorPositionChanged(old_pos: int, new_pos: int)  当光标位置变化时发射此信号，传出旧新光标位置
.selectionChanged()        当选中状态改变时发射此信号，可以通过.selectedText()等方法获取新的选中
.returnPressed()           当用户按下Enter/Return键时发射此信号，当设置了掩码或验证器时只有接受输入才发射
.editingFinished()         按下Enter/Return键、编辑器失去焦点且内容变化时发射此信号
.inputRejected()           当用户输入被验证器拒绝时发射此信号

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-信号")
        self.resize(800, 600)
        self.setup_ui()
        self.signal_test()

    def setup_ui(self) -> None:
        """设置界面"""
        # 创建及初始化控件
        self.line_edit = QtWidgets.QLineEdit(self)
        self.info_label = QtWidgets.QLabel(self)
        button = QtWidgets.QPushButton("用于将焦点移出LineEdit的空白按钮")

        # 通过布局管理器布局控件
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.info_label)
        layout.addWidget(button)
        self.setLayout(layout)

    def signal_test(self) -> None:
        """测试LineEdit的信号"""

        def show_info(info: str) -> None:
            self.info_label.setText(info)
            self.info_label.adjustSize()

        # 测试以下各种信号时，每次只测试一个，注释掉其他
        # self.line_edit.textChanged.connect(lambda text: show_info(f"文本改变为{text}"))  # type: ignore
        self.line_edit.textEdited.connect(lambda text: show_info(f"文本被编辑为{text}"))  # type: ignore
        self.line_edit.setText("通过编程改变的文本")  # 会触发textChanged，但不会触发textEdited

        # self.line_edit.cursorPositionChanged.connect(
        #     lambda old, new: show_info(f"光标由{old}移动到了{new}")
        # )  # type: ignore
        # self.line_edit.selectionChanged.connect(show_info("选择改变了"))  # type: ignore
        # self.line_edit.returnPressed.connect(show_info("用户按下了Enter"))  # type: ignore
        # self.line_edit.editingFinished.connect(show_info("结束编辑"))  # type: ignore

        self.line_edit.setValidator(QtGui.QIntValidator(10, 99, self.line_edit))  # 设置验证器
        self.line_edit.inputRejected.connect(show_info("输入被拒绝了"))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
