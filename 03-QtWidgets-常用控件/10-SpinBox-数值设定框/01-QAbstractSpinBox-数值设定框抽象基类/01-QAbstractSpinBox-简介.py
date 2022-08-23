import sys

from PySide6 import QtCore, QtWidgets

"""
QAbstractSpinBox 数值设定框的抽象基类

官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QAbstractSpinBox.html
继承自QWidget

数值设定框主要用于获取用户输入，用户可以通过右侧箭头加减数值或直接输入数值
抽象基类提供了数值设定框共有的基本功能属性、信号与槽等，本身不能被实例化，主要被
QSpinBox（用于获取整数输入）、QDoubleSpinBox（用于获取浮点数输入）和
QDateTimeEdit（用于获取日期时间）三种子类继承

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractSpinBox-简介")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        # 抽象基类本身不能被实例化，用子类QSpinBox演示

        # 创建一个数值设定框
        spin_box = QtWidgets.QSpinBox()
        spin_box.setRange(0, 99999)  # 设置允许输入的数值范围

        # ========================== 获取并展示用户输入的数值 ==========================
        info_label = QtWidgets.QLabel()  # 用于辅助显示值的标签

        @QtCore.Slot()
        def show_value() -> None:
            """展示spin_box数值的槽函数"""
            info_label.setText(f"用户输入的数值为{spin_box.value()}")
            info_label.adjustSize()

        # 当用户结束编辑（移开光标或按下Enter）后发射信号，展示出输入值
        spin_box.editingFinished.connect(show_value)  # type: ignore

        # 用布局管理器布局控件
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(spin_box)
        layout.addWidget(info_label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
