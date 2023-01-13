"""
QSlider 滑块控件
水平或垂直的滑块
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSlider.html
继承自QAbstractSlider

相比于其抽象父类QAbstractSlider,主要是添加了刻度线功能
"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QSlider")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        slider = QtWidgets.QSlider(self)
        slider.move(200, 200)
        slider.resize(40, 200)

        # 在两侧绘制刻度线
        slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
