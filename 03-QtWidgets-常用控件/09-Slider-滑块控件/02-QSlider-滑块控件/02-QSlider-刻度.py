import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

"""
QSlider 刻度

.setTickPosition(position: QSlider.TickPosition)  设置刻度线位置，见下方QSlider.TickPosition
.tickPosition() -> QSlider.TickPosition           获取刻度线位置

.setTickInterval(ti: int)                         设置刻度线间隔，默认等于PageStep页步长
.tickInterval() -> int                            获取刻度线间隔


QSlider.TickPosition枚举值具体有如下数种：
https://doc.qt.io/qt-6/qslider.html#TickPosition-enum
QSlider.NoTicks           不绘制任何刻度线，默认值
QSlider.TicksBothSides    在滑块两侧都绘制刻度
QSlider.TicksAbove        在水平滑块上方绘制
QSlider.TicksBelow        在水平滑块下方绘制
QSlider.TicksLeft         在垂直滑块左侧绘制
QSlider.TicksRight        在垂直滑块右侧绘制

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QSlider-刻度")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        slider = QtWidgets.QSlider(self)
        slider.move(200, 200)
        slider.resize(40, 200)

        # 设置滑块刻度线位置
        slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        # slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        # slider.setTickPosition(QtWidgets.QSlider.TicksBelow)

        # slider.setOrientation(Qt.Horizontal)  # 将滑块方向设置为水平
        # slider.resize(200, 40)
        # slider.setTickPosition(QtWidgets.QSlider.TicksLeft)
        # slider.setTickPosition(QtWidgets.QSlider.TicksRight)

        # 设置刻度线间距，默认等于PageStep
        slider.setTickInterval(25)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
