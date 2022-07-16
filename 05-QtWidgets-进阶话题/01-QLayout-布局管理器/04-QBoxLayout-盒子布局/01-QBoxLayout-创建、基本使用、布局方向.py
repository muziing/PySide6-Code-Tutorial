import sys

from PySide6 import QtWidgets

"""
QBoxLayout 盒子布局
将子控件沿水平或垂直方向线性排列
继承自QLayout
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QBoxLayout.html

构造函数中必须指定布局方向（见QBoxLayout.Direction），可选地指定父控件
.__init__(self, arg__1: QBoxLayout.Direction, parent: Optional[QWidget] = None)

也可以在创建后更改布局方向：
.setDirection(direction: QBoxLayout.Direction)  将布局的方向设置为 direction

QBoxLayout.Direction枚举值具体包含4种值，涵盖了水平、垂直方向：
https://doc.qt.io/qt-6/qboxlayout.html#Direction-enum
QBoxLayout.LeftToRight    水平从左至右
QBoxLayout.RightToLeft    水平从右至左
QBoxLayout.TopToBottom    垂直从上至下
QBoxLayout.BottomToTop    垂直从下至上

QBoxLayout有两个子类：QHBoxLayout与QVBoxLayout，行为与QBoxLayout几乎完全一样，只是指定了方向
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QBoxLayout-盒子布局")
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建待布局的控件
        # 此处无需指定父控件，添加至布局管理器后自动成为self的子控件
        button_1 = QtWidgets.QPushButton("One")
        button_2 = QtWidgets.QPushButton("Two")
        button_3 = QtWidgets.QPushButton("Three")
        button_4 = QtWidgets.QPushButton("Four")
        button_5 = QtWidgets.QPushButton("Five")

        # 创建布局管理器对象，创建时指定布局方向为垂直从上至下
        layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)

        # 将控件添加到布局管理器中
        layout.addWidget(button_1)
        layout.addWidget(button_3)
        layout.addWidget(button_4)
        layout.addWidget(button_5)
        layout.insertWidget(1, button_2)

        # 将布局方向设置为水平从左至右
        layout.setDirection(QtWidgets.QBoxLayout.LeftToRight)

        # 为主窗口设置布局管理器
        # 同时将self设置为了layout、layout中被管理的控件的父控件
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
