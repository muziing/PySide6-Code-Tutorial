import random
import sys

# 导入所需的模块
from PySide6 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["你好世界", "Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        # 创建一个按钮控件，其上文字为“点击我”
        self.button = QtWidgets.QPushButton("点击我！")
        # 创建一个标签控件，内容为Hello World,对齐方式为居中
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        # 创建一个「垂直盒子」布局管理器
        self.layout = QtWidgets.QVBoxLayout(self)

        # 将之前创建的控件添加到布局管理器中，即完成布局
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        # 将button.clicked这个信号与self.magic槽函数连接
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self) -> None:
        """槽函数"""
        self.text.setText(random.choice(self.hello))  # 从列表中随机显示一条问候语


if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # 创建APP

    widget = MyWidget()  # 实例化一个MyWidget类对象
    widget.resize(800, 600)  # 设置窗口大小，单位为像素
    widget.show()  # 显示窗口

    sys.exit(app.exec())  # 正常退出APP
