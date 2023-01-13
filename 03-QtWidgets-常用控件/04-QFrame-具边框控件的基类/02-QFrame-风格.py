"""
QFrame 风格：形状、阴影、线宽
所有组合的视觉效果：https://doc.qt.io/qt-6/images/frames.png

由形状、阴影组合成风格

.setFrameStyle(style: int)        设置风格，即边框形状与阴影的组合
.setFrameShape(QFrame.Shape)      设置边框的形状，详见下文QFrame.Shape
.setFrameShadow(QFrame.Shadow)    设置边框阴影，详见下文QFrame.Shadow
.setLineWidth(int)                设置线宽，默认值为1
.setMidLineWidth(int)             设置中线的宽度，默认值为0

.frameShape() -> QFrame.Shape     获取边框形状
.frameWidth() -> int              获取整个边框的宽度，边框形状为HLine或VLine时的宽度
.lineWidth() -> int               获取线宽
.midLineWidth() -> int            获取中线宽

QFrame.Shape 枚举值具体有如下数种：
https://doc.qt.io/qt-6/qframe.html#Shape-enum
QFrame.NoFrame        QFrame什么都不绘制
QFrame.Box            沿着其内容绘制一个盒子（边框）
QFrame.Panel          绘制一个面板以使内容浮起或下沉
QFrame.StyledPanel    绘制一个矩形面板，其形状由当前的GUI风格决定，可能是浮起或下沉
QFrame.HLine          绘制一条水平的线，不作为任何东西的边框
QFrame.VLine          绘制一条垂直的线，不作为任何东西的边框
QFrame.WinPanel       绘制一个可以像Windows2000中的面板那样浮起或下沉的矩形面板


QFrame.Shadow 枚举值具体有如下数种：
https://doc.qt.io/qt-6/qframe.html#Shadow-enum
QFrame.Plain          边框与内容与周围处于同水平，没有任何3D效果
QFrame.Raised         边框与内容浮起，使用当前的颜色组绘制亮处与阴影以实现3D效果
QFrame.Sunken         边框与内容下沉，使用当前的颜色组绘制亮处与阴影以实现3D效果
"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QFrame-风格")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        frame = QtWidgets.QFrame(self)
        frame.resize(200, 200)
        frame.move(200, 200)

        # frame.setFrameStyle(QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Raised)
        frame.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        frame.setLineWidth(3)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
