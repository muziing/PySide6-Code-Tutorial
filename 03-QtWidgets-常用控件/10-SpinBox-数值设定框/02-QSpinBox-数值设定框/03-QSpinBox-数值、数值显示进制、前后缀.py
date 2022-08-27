import sys

from PySide6 import QtWidgets

"""
QSpinBox

=================================== 数值 ===================================
可以直接获取、直接设置spinbox中的数值
若设置的新数值与之前的不同，则会发射valueChanged()信号

.satValue(val: int)
.value() -> int

=================================== 数值显示进制 ===================================
数值设定框中的数默认以十进制显示，也可以设置为其他进制
注意此属性只形象显示效果，仍然以十进制处理

.setDisplayIntegerBase(base: int)
.displayIntegerBase() -> int

=================================== 前后缀 ===================================
在数值设定框的LineEdit中，除了显示纯数值，还可以为数值添加前后缀，
实现例如 $200、45kg 等效果。
注意调用text()方法时会获取包含前后缀的完整文本，而cleanText()可获取纯数值

.setPrefix(prefix: str)         设置前缀字符串
.setSuffix(suffix: str)         设置后缀字符串
.prefix() -> str                获取前缀
.suffix() -> str                获取后缀
.cleanText() -> str             获取不含前后缀的纯文本


"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QSpinBox")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        spinbox = QtWidgets.QSpinBox(self)
        spinbox.move(200, 200)
        spinbox.setRange(0, 1000)

        # 设置数值
        spinbox.setValue(88)

        # 设置显示数值进制
        spinbox.setDisplayIntegerBase(16)  # 设置为16进制
        spinbox.setPrefix("0x")  # 添加前缀便于用户理解

        # 设置前后缀
        spinbox.setSuffix(" cm")  # 设置后缀
        # spinbox.setPrefix("$ ")  # 设置前缀
        print(f"完整文本为{spinbox.text()}")  # 获取文本时会获取到包含前后缀的完整文本
        print(f"数值为{spinbox.text().removesuffix(spinbox.suffix())}")  # Python3.9提供的移除后缀方法
        print(f"数值为{spinbox.cleanText()}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
