import sys

from PySide6 import QtCore, QtWidgets

"""
QAbstractSlider 滑块类控件的基类
用户可以通过滑块来输入整形数据
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QAbstractSlider.html
继承自QWidget

本身为抽象基类，不能被实例化，主要有QSlider滑块、QDial旋钮、QScrollBar滚动条三个子类
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractSlider")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 滑块
        slider = QtWidgets.QSlider(self)
        slider.move(200, 200)

        # 旋钮
        dial = QtWidgets.QDial(self)
        dial.move(360, 200)

        info_label = QtWidgets.QLabel(self)
        info_label.move(240, 200)

        @QtCore.Slot(int)
        def test(value: int):
            info_label.setText(f"滑块的值变成了{value}")
            info_label.adjustSize()

        # 连接信号与槽，显示用户通过滑块/旋钮输入的值
        # slider.valueChanged.connect(test)  # type: ignore
        dial.valueChanged.connect(test)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
