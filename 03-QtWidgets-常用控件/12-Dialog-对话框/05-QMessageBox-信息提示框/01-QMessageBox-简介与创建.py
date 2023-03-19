import sys

from PySide6 import QtWidgets

"""
QMessageBox 信息提示框

信息提示框是一种模态对话框，用于向用户提示信息，或向用户提出一个问题并接收回答
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMessageBox.html
继承自QDialog


有两种构造函数，简易版可选传入父控件，完整版则可以在创建时设置几乎所有属性：

.__init__(self, parent: Optional[QWidget] = None)

.__init__(self, icon: QMessageBox.Icon, title: str, text: str, \
buttons: QMessageBox.StandardButtons = QMessageBox.StandardButton.NoButton, parent: Optional[QWidget] = None, \
flags: Qt.WindowFlags = Instance(Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint))

若只需临时使用一次对话框，显式创建实例并调用.open()的操作，可以用静态方法替代，详情见本目录下对应小节

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QMessageBox-信息提示框")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 第一种构造函数
        # message_box = QtWidgets.QMessageBox(self)
        # message_box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        # message_box.setWindowTitle("这是一个消息提示框")
        # message_box.setText("您不能在关闭模态对话框前操作其他窗口！")
        # message_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        # 以上设置等价于第二种构造函数：
        message_box = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Warning,
            "这是一个消息提示框",
            "您不能在关闭模态对话框前操作其他窗口！",
            QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel,
            self,
        )

        pop_btn = QtWidgets.QPushButton("弹出对话框", self)
        pop_btn.move(200, 200)
        pop_btn.clicked.connect(message_box.open)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
