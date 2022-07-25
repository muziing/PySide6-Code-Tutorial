import sys

from PySide6 import QtCore, QtWidgets

"""
QDial 旋钮控件
圆形的范围控制控件，类似于电位器或速度表
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDial.html
继承自QAbstractSlider

只有一种构造函数，可以设置父控件
.__init__(self, parent: Optional[QWidget] = None)
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QDial")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        dial = QtWidgets.QDial(self)
        dial.move(200, 200)

        info_label = QtWidgets.QLabel(self)
        info_label.move(320, 230)

        @QtCore.Slot(int)
        def show_value(value: int):
            info_label.setText(f"旋钮的值变成了{value}")
            info_label.adjustSize()

        dial.valueChanged.connect(show_value)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
