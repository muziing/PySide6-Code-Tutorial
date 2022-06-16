import random
import sys

# 导入所需的模块
from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 调用父类的初始化方法

        self.hello = ["你好世界", "Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # 设置窗口大小，单位为像素
        self.resize(800, 600)

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
        self.button.clicked.connect(self.magic)  # type: ignore

    @QtCore.Slot()
    def magic(self) -> None:
        """槽函数"""
        self.text.setText(random.choice(self.hello))  # 从列表中随机显示一条问候语


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
    widget = MyWidget()  # 实例化一个MyWidget类对象
    widget.show()  # 显示窗口
    sys.exit(app.exec())  # 正常退出APP：app.exec()关闭app，sys.exit()退出进程
