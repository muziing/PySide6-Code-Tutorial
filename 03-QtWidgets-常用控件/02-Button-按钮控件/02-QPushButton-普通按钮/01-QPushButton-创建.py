import sys

from PySide6 import QtGui, QtWidgets

"""
QPushButton 普通按钮
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPushButton.html

构造函数：
QPushButton(parent = None)                单个参数，父对象默认值为None
QPushButton(text[, parent = None])        两个参数，指定按钮上的文字
QPushButton(icon, text[, parent = None])  三个参数，指定按钮上的图标和文字

即使创建时未指定父对象、文字、图标，仍可通过调用对应方法设定
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPushButton-创建")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        icon = QtGui.QIcon("../../../Resources/Icons/Python_128px.png")
        # 1. 单个参数
        # button = QtWidgets.QPushButton()
        # button.setParent(self)  # 创建时父对象为None,可用setParent方法指定
        # button.setText("普通按钮")  # 设置按钮上的文字
        # button.setIcon(icon)  # 设置按钮上的图标

        # 2. 两个参数
        # button = QtWidgets.QPushButton("普通按钮", self)

        # 3. 三个参数
        button = QtWidgets.QPushButton(icon, "普通按钮", self)

        button.resize(150, 50)  # 调整按钮尺寸
        # 通过计算需要移动的尺寸，令按钮居中
        button.move((self.width() - button.width()) // 2, (self.height() - button.height()) // 2)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
