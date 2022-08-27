import sys

from PySide6 import QtWidgets

"""
QDoubleSpinBox 浮点数值设定框

与QSpinBox控件非常相似，只是数据类型为double
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDoubleSpinBox.html
继承自QAbstractSpinBox

各种属性、方法与QSpinBox几乎完全一致，请读者参考QSpinBox小节
此处只列出QDoubleSpinBox特有的属性方法

可以设置小数位数，注意不要超过double数据类型自身限制决定的最大上限
.setDecimals(prec: int)
.decimals() -> int

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QDoubleSpinBox")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        d_spinbox = QtWidgets.QDoubleSpinBox(self)
        d_spinbox.move(200, 200)

        d_spinbox.setDecimals(3)  # 显示3位小数
        d_spinbox.valueChanged.connect(lambda val: print(f"值变成了{val}"))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
