import sys

from PySide6 import QtWidgets

"""
QSpinBox 信号

除继承自父类的editingFinished信号，QSPinBox还有两个关于值变化的信号：

textChanged(text: str)     当数值设定框中的文本发生改变时发射此信号，新的文本（包含前后缀）作为参数传出
valueChanged(i: int)       当数值设定框的值发生改变时发射此信号，新的值作为参数传递

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QSpinBox-信号")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面与测试功能"""
        spinbox = QtWidgets.QSpinBox(self)
        spinbox.move(200, 200)

        spinbox.textChanged.connect(lambda text: print(f"文本变成了{text}"))  # type: ignore
        spinbox.valueChanged.connect(lambda val: print(f"值变成了{val}"))  # type: ignore

        spinbox.setValue(50)
        spinbox.setPrefix("￥")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
