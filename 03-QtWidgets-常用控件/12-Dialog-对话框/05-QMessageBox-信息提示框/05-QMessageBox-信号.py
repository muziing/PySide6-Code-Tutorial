import sys

from PySide6 import QtWidgets

"""
QMessageBox 信号

除继承自父类的信号，QMessageBox只有一种信号：

.buttonClicked(button: QAbstractButton)  当信息提示框中的按钮被点击时发射此信号，按钮作为参数传出

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QMessageBox-信号")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建对话框
        message_box = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Warning,
            "这是一个消息提示框",
            "您不能在关闭模态对话框前操作其他窗口！",
            QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel,
            self,
        )

        # 测试信号：将获取到的按钮的文本打印到终端
        message_box.buttonClicked.connect(lambda btn: print(btn.text()))  # type: ignore

        # 在主界面上弹出对话框
        pop_btn = QtWidgets.QPushButton("弹出对话框", self)
        pop_btn.move(200, 200)
        pop_btn.clicked.connect(message_box.open)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
