import sys

from PySide6 import QtWidgets

"""
QSpinBox 数值设定框

QSpinBox 主要用于接收用户输入的整数型数据
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSpinBox.html
继承自 QAbstractSpinBox

只有一种构造函数，可以将父对象作为参数传入
.__init__(self, parent: Optional[QWidget] = None)

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QSpinBox-数值设定框")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        spinbox = QtWidgets.QSpinBox(self)
        spinbox.resize(100, 35)
        spinbox.move((self.width() - spinbox.width()) // 2, (self.height() - spinbox.height()) // 2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
