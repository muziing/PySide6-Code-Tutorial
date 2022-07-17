import sys

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

"""
QScrollArea 视图控件
QScrollArea主要功能在于将另一个控件滚动着显示，被显示的控件在本文中暂且称为「视图控件」
可能需要对视图控件调用 QWidget.setMinimumSize() 以确保控件的内容正确显示在滚动区域内

============================== 设置与获取控件 =========================
调用如下方法以将控件设置为滚动区域的视图控件，或获取、移除滚动区域的视图控件

.setWidget(widget: QWidget)          将widget设置为滚动区域的视图控件
.widget() -> QWidget                 返回滚动区域的视图控件
.takeWidget() -> QWidget             移除滚动区域的视图控件，并将该控件的所有权传递给函数调用者

============================== 对齐方式 =========================
当视图控件尺寸小于滚动区域尺寸时，可以控制视图控件在整个滚动区域中的对齐方式，默认值为对齐至左上
Qt.Alignment 具体取值参考本项目00-01-Qt命名空间

.setAlignment(Qt.Alignment)          设置视图控件在滚动区域中的对齐方式，默认为左上
.alignment() -> Qt.Alignment         返回视图控件在滚动区域中的对齐方式

============================== 尺寸控制 =========================
默认情况下，视图控件大小不可调整大小(False)，滚动区域遵循其尺寸，可以通过widget.resize()
调整视图控件尺寸，滚动区域将自动调整到新的尺寸。
若此属性设置为True，则滚动区域将自动调整视图控件的尺寸，以尽可能避免出现滚动条，或
利用额外的空间

.setWidgetResizable(resizable: bool) 设置视图控件可以改变尺寸，默认为False
.widgetResizable() -> bool           获取视图控件尺寸可变状态

============================== 确保可见 =========================
可以通过调用方法滚动内容，确保滚动区域中的，某点或某子控件出现在滚动区域的可见视口内
通过xmargin和ymargin参数控制边距，单位为像素。如果无法达到指定点/子控件，则将
内容滚动到最近的有效位置。

.ensureVisible(x: int, y: int, xmargin: int = 50, ymargin: int = 50)               确保视图控件内某点可见
.ensureWidgetVisible(child_widget: QWidget, xmargin: int = 50, ymargin: int = 50)  确保视图控件的某个子控件可见

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QScrollArea-视图控件")
        self.resize(800, 600)
        self.setup_ui()

        # 注意test_01与test_02互斥，测试一项时需要注释掉另一项
        # self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""

        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.move(50, 50)
        image_label = QtWidgets.QLabel(self.scroll_area)
        image_label.setPixmap(QtGui.QPixmap("../../Resources/Images/Python-code.jpg"))

        # 将图像标签设置为滚动区域的视图控件
        self.scroll_area.setWidget(image_label)

        # 测试取出视图控件功能
        # print(self.scroll_area.takeWidget())  将视图控件从滚动区域中移除，并返回

    def test_01(self) -> None:
        """测试对齐方式、获取控件功能"""

        # 手动指定滚动区域尺寸，而不是由视图控件自动设置
        self.scroll_area.resize(600, 500)

        # 获取滚动区域的视图控件，并设置其尺寸小于滚动区域，需要考虑对齐方式
        self.scroll_area.widget().resize(200, 400)  # 尺寸小于滚动区域尺寸

        # 设置对齐方式
        self.scroll_area.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # 设置为水平居中、垂直靠底部对齐

    def test_02(self) -> None:
        """测试尺寸控制、确保可见功能"""

        self.scroll_area.widget().resize(200, 400)  # 设置了视图控件为较小的尺寸

        # 启用滚动区域调整其视图控件尺寸的功能
        self.scroll_area.setWidgetResizable(True)  # 滚动区域将放大其视图控件尺寸，以充分利用空间
        # 默认行为为将小尺寸的视图控件显示在大尺寸的滚动区域中，浪费空间

        self.scroll_area.ensureVisible(888, 710)  # 滚动区域将自动滚动，确保指定的点能显示在视口中


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
