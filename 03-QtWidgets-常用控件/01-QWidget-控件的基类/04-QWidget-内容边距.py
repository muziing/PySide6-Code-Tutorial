import sys

from PySide6 import QtWidgets

"""
Margins 边距
QWidget.setContentsMargins(int left, int top, int right, int bottom)
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget 内容边距的设定")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self) -> None:
        """测试设置边距功能"""
        label = QtWidgets.QLabel(self)
        label.setText("ABC ABC ABC ABC")
        label.resize(300, 300)
        # 设置背景颜色，便于观察label控件的实际大小
        label.setStyleSheet("background-color: cyan; font-size: 30px;")

        # 设置内容边距，距离左上角100 200像素
        label.setContentsMargins(100, 200, 0, 0)

        # 获取边距
        print(label.contentsMargins())
        print(label.contentsRect())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
