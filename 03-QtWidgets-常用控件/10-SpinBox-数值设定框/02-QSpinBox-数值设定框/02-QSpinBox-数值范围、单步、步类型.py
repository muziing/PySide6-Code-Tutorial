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

=================================== 步类型 ===================================
除指定单步步长外，还可以通过将步类型改变为「自适应小数步」来调整步长
启用AdaptiveDecimalStepType自适应小数步后，步长将变成当前值的低一位，
例如当前值为12000，则步长变为1000；当前值为120，步长变为10
更多详细信息请参考文档：https://doc.qt.io/qt-6/qspinbox.html#setStepType

.setStepType(QAbstractSpinBox.StepType)
.stepType() -> QAbstractSpinBox.StepType

QAbstractSpinBox.StepType枚举值有如下两种类型：
https://doc.qt.io/qt-6/qabstractspinbox.html#StepType-enum
QAbstractSpinBox.StepType.DefaultStepType
QAbstractSpinBox.StepType.AdaptiveDecimalStepType
"""

import sys

from PySide6 import QtWidgets


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
        # spinbox.setRange(10, 2000)  # 等价于下面两行
        spinbox.setMaximum(2000)
        spinbox.setMinimum(10)
        print(f"数值范围的最大值为{spinbox.maximum()}")

        # 设置单步步长
        spinbox.setSingleStep(10)  # 每次增加/减少10
        print(f"目前的单步步长为{spinbox.singleStep()}")

        # 设置步类型
        # 注意启用自适应小数步后，之前设置的单步步长失效
        spinbox.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
