import sys

from PySide6 import QtWidgets

"""
QDialog 对话框类
对话框是一类用于与用户交互的控件，往往作为单独的窗口弹出
可以向用户展示信息（例如QMessageBox）、获取用户的选择（如通过QFileDialog获取用户选择的文件）等
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDialog.html
QDialog继承自QWidget，是所有对话框控件的基类

只有一种构造函数，可选地将父控件传入
.__init__(self, parent: Optional[PySide6.QtWidgets.QWidget]

注意对话框控件设置父控件略有特殊：对话框始终为独立窗口（而不会成为父控件的一部分）、
如果为对话框设置了父控件，则其默认出现在父控件的顶级控件的上方（窗口在最上方，可以盖住下面
的内容；它还将共享父级的任务栏条目
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QDialog")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 设置对话框
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("这是一个对话框")
        dialog.resize(300, 200)
        QtWidgets.QLabel("模态对话框会影响主窗口关闭", dialog)

        # 在主窗口上弹出对话框
        test_btn = QtWidgets.QPushButton("弹出对话框", self)
        test_btn.move(200, 200)
        test_btn.clicked.connect(dialog.exec)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
