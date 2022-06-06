import sys

from PySide6 import QtWidgets

"""
QWidget
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html
1.所有可视控件的基类
2.是一个最简单的空白控件
3.控件是用户界面的最小元素
4.每个控件都是矩形的，它们按Z轴顺序排序
5.控件由其父控件和前面的控件裁剪
6.没有父控件的控件，称之为窗口
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self创建时未传入父控件，故成为窗口
        # 窗口会被自动修饰标题、最小化最大化关闭按钮等，称为「框架」，可以手动修改其行为
        self.setWindowTitle("QWidget简介")  # 设置窗口标题
        self.resize(800, 600)  # 设置大小
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建一个名为red的QWidget
        red = QtWidgets.QWidget(self)  # red的父控件为self,故不成为单独窗口
        red.resize(100, 100)
        red.setStyleSheet("background-color: red;")
        red.move(300, 100)

        # 创建一个名为green的QWidget
        green = QtWidgets.QWidget(self)
        green.resize(100, 100)
        green.setStyleSheet("background-color: green;")
        green.move(300, 150)  # 体现QWidget沿z轴绘制，后面的控件可以覆盖前面的控件


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
