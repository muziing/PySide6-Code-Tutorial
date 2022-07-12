import sys

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

"""
QAbstractScrollArea 滚动条控件、角落控件

作为一个复合控件，QAbstractScrollArea 可以单独设置和获取其中的水平滚动条、
垂直滚动条、位于两个滚动条之间的角落控件
QScrollBar 官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QScrollBar.html


.setHorizontalScrollBar(scrollbar: QScrollBar)                    设置水平滚动条
.setVerticalScrollBar(scrollbar: QScrollbar)                      设置垂直滚动条
.horizontalScrollBar() -> QScrollBar                              获取水平滚动条
.verticalScrollBar() -> QScrollBar                                获取垂直滚动条

.addScrollBarWidget(widget: QWidget, alignment: Qt.Alignment)     在指定的对齐方式的位置添加控件作为滚动条控件
.scrollBarWidgets(alignment: Qt.Alignment) -> List[QWidget]       返回当前设置的滚动条控件的列表

.setCornerWidget(widget: QWidget)                                 设置角落控件
.cornerWidget() -> QWidget                                        获取角落控件

"""


class Window(QtWidgets.QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractScrollArea-滚动条与角落控件")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.resize(600, 400)
        self.move(100, 100)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        image_label = QtWidgets.QLabel(self)
        image_label.setPixmap(QtGui.QPixmap("../../Resources/Images/Python-code.jpg"))
        self.setWidget(image_label)

    def test_01(self) -> None:
        """测试设置滚动条功能"""
        scrollbar = QtWidgets.QScrollBar(self)  # 创建自己的进度条控件
        self.setVerticalScrollBar(scrollbar)  # 将该进度条控件设置给self

        hsb = self.horizontalScrollBar()  # 获取水平进度条
        hsb.setValue(500)  # 设置位置为100（默认为0）

    def test_02(self) -> None:
        """测试设置角落控件功能"""
        label = QtWidgets.QLabel(self)
        label.setPixmap(QtGui.QPixmap("../../Resources/Icons/Python_128px.png"))
        label.setScaledContents(True)
        self.setCornerWidget(label)  # 水平滚动条与垂直滚动条之间的角落显示该图标
        print(self.cornerWidget())  # 获取角落控件


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
