import sys

from PySide6 import QtCore, QtWidgets

"""
QWidget 可以设置不可见与不可用

窗口上的控件被设置为不可见后被隐藏，但不会被释放，仍占据原先的位置
.setVisible()   设置可见/不可见
.isVisible()    获取可见状态
.hide()         设为不可见，等同于.setVisible(False)
.show()         对于非窗口的控件，等同于.setVisible(True)

对于编辑器、按钮、下拉框等控件可以设置不可用，用户不再能与之交互
.setEnabled()   设置可用/不可用
.isEnabled()    获取可用状态
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget-不可见与不可用")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.label = QtWidgets.QLabel("标签", self)
        self.label.resize(200, 200)
        self.label.setStyleSheet("background-color: cyan;")
        self.label.move(50, 50)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.move(500, 50)
        self.text_edit.setPlaceholderText("这是一个文本编辑器")

        self.button_1 = QtWidgets.QPushButton("切换可见状态", self)
        self.button_1.move(300, 50)

        self.button_2 = QtWidgets.QPushButton("切换可用状态", self)
        self.button_2.move(300, 150)

    def test_01(self) -> None:
        """测试可见与不可见"""

        @QtCore.Slot()
        def test_slot() -> None:
            if self.label.isVisible():
                self.label.setVisible(False)
            else:
                self.label.setVisible(True)

        self.button_1.clicked.connect(test_slot)  # type: ignore

    def test_02(self) -> None:
        """测试可用与不可用"""

        @QtCore.Slot()
        def test_slot() -> None:
            if self.text_edit.isEnabled():
                self.text_edit.setEnabled(False)
            else:
                self.text_edit.setEnabled(True)

        self.button_2.clicked.connect(test_slot)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
