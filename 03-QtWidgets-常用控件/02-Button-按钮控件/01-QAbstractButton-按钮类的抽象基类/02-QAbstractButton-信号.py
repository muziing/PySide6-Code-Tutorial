import sys

from PySide6 import QtCore, QtWidgets

"""
QAbstractButton 信号

当按钮与用户交互时，发射信号，有如下数种信号可选：

1. clicked    光标在按钮上时按下鼠标主键，并在不离开按钮前提下抬起，才发射本信号
2. pressed    按下按钮时触发
3. released   松开按钮时触发
4. toggled    按钮状态改变时触发（单选按钮、复选框等）

建议阅读Qt6文档以获取更多信息：https://doc.qt.io/qt-6/qabstractbutton.html#clicked
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractButton-信号")
        self.resize(800, 600)
        self.setup_ui()
        self.test()

    def setup_ui(self) -> None:
        """设置界面"""
        # 由于QAbstractButton类无法被实例化，用QPushButton演示
        self.button = QtWidgets.QPushButton("点击我！", self)
        self.button.move(350, 300)  # 移动按钮控件的位置

    def test(self) -> None:
        """测试信号"""

        @QtCore.Slot()
        def test_slot() -> None:
            print("按钮被交互了！")

        # 1.clicked: 点击（按下并松开）时发射
        self.button.clicked.connect(test_slot)  # type: ignore

        # 2.pressed: 按下时发射
        # self.button.pressed.connect(test_slot)  # type: ignore

        # 3.released: 抬起时发射
        # self.button.released.connect(test_slot)  # type: ignore

        # 4.toggled: 状态改变时发射

        # @QtCore.Slot(bool)
        # def test_toggled(value: bool) -> None:
        #     print("按钮选中状态发生了变化", value)
        #     # 可以根据value的值编写对应逻辑功能的代码
        #
        # self.button.setCheckable(True)  # 使得按钮可以被选中
        # self.button.toggled.connect(test_toggled)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
