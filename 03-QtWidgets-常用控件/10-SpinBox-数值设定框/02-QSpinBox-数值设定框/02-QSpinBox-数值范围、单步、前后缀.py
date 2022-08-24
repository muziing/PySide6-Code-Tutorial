import sys

from PySide6 import QtWidgets

"""
QSpinBox

=================================== 数值范围 ===================================
数值设定框允许接受的数值范围可以通过编程指定
注意可以通过组合最小值和specialValueText属性实现特殊功能

.setRange(min: int, max: int)   设置数值范围，与分别设置最小最大值等价
.setMaximum(max: int)           设置最大值，默认值为99
.setMinimum(min: int)           设置最小值，默认值为0
.maximum() -> int               获取最大值
.minimum() -> int               获取最小值

=================================== 单步 ===================================
当用户使用箭头来增加/减少数值设定框中的值时，每次会改变一个单步（single step）
默认单步步长为1，即每次增加/减少1，也可以设定为其他正数值

.setSingleStep(val: int)        设置单步步长
.singleStep() -> int            获取当前单步步长


=================================== 前后缀 ===================================
在数值设定框的LineEdit中，除了显示纯数值，还可以为数值添加前后缀，
实现例如 $200、45kg 等效果。注意调用text()方法时会获取包含前后缀的完整文本

.setPrefix(prefix: str)         设置前缀字符串
.setSuffix(suffix: str)         设置后缀字符串
.prefix() -> str                获取前缀
.suffix() -> str                获取后缀

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QSpinBox")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面与测试功能"""

        spinbox = QtWidgets.QSpinBox(self)
        spinbox.move(200, 200)

        # 设置数值范围
        # spinbox.setRange(100, 200)  # 等价于下面两行
        spinbox.setMaximum(200)
        spinbox.setMinimum(100)
        print(f"数值范围的最大值为{spinbox.maximum()}")

        # 设置单步步长
        spinbox.setSingleStep(10)  # 每次增加/减少10
        print(f"目前的单步步长为{spinbox.singleStep()}")

        # 设置前后缀
        spinbox.setSuffix(" cm")  # 设置后缀
        # spinbox.setPrefix("$ ")  # 设置前缀
        print(f"完整文本为{spinbox.text()}")  # 获取文本时会获取到包含前后缀的完整文本
        print(f"数值为{spinbox.text().removesuffix(spinbox.suffix())}")  # Python3.9提供的移除后缀方法


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
