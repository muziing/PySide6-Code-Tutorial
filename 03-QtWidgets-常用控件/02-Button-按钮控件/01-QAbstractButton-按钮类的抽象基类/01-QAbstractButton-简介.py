import sys

from PySide6 import QtGui, QtWidgets

"""
QAbstractButton 按钮控件的基类

官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QAbstractButton.html

1. 提供按钮类通用的方法，如设置文字图标、被点击、键盘快捷键等
2. 自身不能被实例化，子类可以被实例化
3. 被 QPushButton、QRadioButton、QCheckBox 等类继承
"""


class MyButton(QtWidgets.QAbstractButton):
    """自定义的按钮控件，体验从按钮抽象基类继承"""

    def paintEvent(self, evt) -> None:
        """重写了父类的paintEvent"""

        # print("绘制")  # 取消本行注释，可观察绘制事件发生的时刻

        # 绘制按钮上要展示的一个界面内容，手动绘制
        painter = QtGui.QPainter(self)  # 创建一个画家；告诉画在什么地方
        pen = QtGui.QPen(QtGui.QColor(20, 154, 151), 5)  # 创建并设置一个笔
        painter.setPen(pen)  # 把笔给画家
        painter.drawText(20, 70, self.text())  # 把按钮文字画在按钮上
        painter.drawEllipse(5, 5, 100, 120)  # 画个椭圆


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractButton-简介")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建一个自定义按钮控件，其父控件为MyWidget
        button = MyButton(self)
        button.setText("自定义按钮")  # 设置按钮上的文字
        button.resize(150, 150)
        button.move(100, 100)  # 移动按钮控件的位置

        # 将按钮被点击的信号与lambda槽函数连接
        button.clicked.connect(lambda: print("按钮被点击了"))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
