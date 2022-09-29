import sys

from PySide6 import QtWidgets

"""
QErrorMessage 错误信息提示框
用于向用户交互展示程序发生的错误，或者用于debug
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QErrorMessage.html
继承自QDialog


只有一种构造函数，可选地将父控件传入
.__init__(self, parent: Optional[QtWidgets.QWidget] = None)

调用showMessage方法即可展示错误信息，如果用户已经勾选了「不再提示」则该函数不生效
.showMessage(message: str)
.showMessage(message: str, type: str)

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QErrorMessage")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        error_message = QtWidgets.QErrorMessage(self)
        error_message.setWindowTitle("错误提示")
        error_message.showMessage("程序出现了错误")
        error_message.showMessage("程序出现了错误")
        error_message.showMessage("程序出现了其他错误")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
