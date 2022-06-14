import sys

from PySide6 import QtCore, QtWidgets

"""
QWidget 有层级关系（z轴）
默认情况下，后绘制的控件会遮盖先绘制的控件
可以通过API调整层级关系

.lower()                降低层级
.raise_()               提高层级(注意为避免和关键字冲突，末尾有下划线)
.stackUnder(QWidget q)  将自身置于q之下
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget-层级关系")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()

    def setup_ui(self) -> None:
        """设置界面"""
        self.label_1 = QtWidgets.QLabel("标签1", self)
        self.label_1.resize(200, 200)
        self.label_1.setStyleSheet("background-color: red;")

        # 默认情况下，后绘制的控件会覆盖先绘制的
        self.label_2 = QtWidgets.QLabel("标签2", self)
        self.label_2.resize(200, 200)
        self.label_2.setStyleSheet("background-color: green;")
        self.label_2.move(50, 50)

    def test_01(self) -> None:
        """测试调整层级关系功能"""
        button = QtWidgets.QPushButton("显示标签1", self)
        button.move(400, 100)

        @QtCore.Slot()
        def test_slot() -> None:
            """按钮的槽函数"""
            # 以下三种方法之一，都可以使得label_1显示在前面
            # self.label_2.lower()  # 降低label_2的层级
            # self.label_1.raise_()  # 提高label_1的层级
            self.label_2.stackUnder(self.label_1)  # 使得2在1之下

        # 连接按钮点击信号与槽函数
        button.clicked.connect(test_slot)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
