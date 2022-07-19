import sys

from PySide6 import QtCore, QtWidgets

"""
QLineEdit 编辑操作-选中

单行文本编辑器的编辑操作中有许多关于选中的方法

.hasSelectedText() -> bool    返回编辑器中是否有文本被选中
.selectedText() -> str        返回被选中的文本
.selectionStart() -> int      返回选中文本的起始位置，若没有选中则返回-1
.selectionEnd() -> int        返回选中文本的结束位置，若没有选中则返回-1
.selectionLength() -> int     返回选中文本的长度

.setSelection(start: int, length: int)  从start开始选中长度为length的文本，length允许为负数
.deselect()                   取消选中任何已被选中的文本

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-选中")
        self.resize(500, 400)
        self.setup_ui()
        self.test()

    def setup_ui(self) -> None:
        """设置界面"""

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setText("测试选中状态")
        self.info_pte = QtWidgets.QPlainTextEdit()
        self.info_pte.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.info_pte)
        self.setLayout(layout)

    def test(self):
        """测试选中功能"""

        @QtCore.Slot()
        def test_slot():
            info_text = (
                f"选中的文本为：{self.line_edit.selectedText()}\n"
                f"选中起始位置为：{self.line_edit.selectionStart()}\n"
                f"选中结束位置为：{self.line_edit.selectionEnd()}\n"
                f"选中长度为：{self.line_edit.selectionLength()}\n"
            )
            self.info_pte.setPlainText(info_text)

        self.line_edit.selectionChanged.connect(test_slot)  # type: ignore

        # 设置选中文本
        self.line_edit.setSelection(0, 100)  # 参数：起始位置、长度

        # 取消选中文本
        # self.line_edit.deselect()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
