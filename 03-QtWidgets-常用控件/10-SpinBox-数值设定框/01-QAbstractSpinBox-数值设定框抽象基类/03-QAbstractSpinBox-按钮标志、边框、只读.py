"""
QAbstractSpinBox 按钮标志、边框、只读

=================================== 按钮标志 ===================================
可以控制数值设定框右侧的按钮的图标，默认为上下箭头
如果需要精细美化界面，可以使用QSS控制用自定义图标替换默认图标

.setButtonSymbols(bs: QAbstractSpinBox.ButtonSymbols)
.buttonSymbols() -> QAbstractSpinBox.ButtonSymbols

QAbstractSpinBox.ButtonSymbols枚举值具体有如下数种：
https://doc.qt.io/qt-6/qabstractspinbox.html#ButtonSymbols-enum
QAbstractSpinBox.ButtonSymbols.UpDownArrows    经典风格中的向上/向下小箭头
QAbstractSpinBox.ButtonSymbols.PlusMinus       加号+与减号-
QAbstractSpinBox.ButtonSymbols.NoButtons       不显示任何按钮

=================================== 边框 ===================================
可以调整SpinBox外观是否具有边框，默认为具有边框

.setFrame(yes: bool)
.hasFrame() -> bool

=================================== 只读 ===================================
可以设置数值设定框为只读模式，用户不可编辑调整，QLineEdit也不再显示光标
与不可用的区别在于，只读模式下可以选中LineEdit中的文本，不可用模式下不可以

.setReadOnly(r: bool)
.isReadOnly() -> bool
"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractSpinBox")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面与测试功能"""

        spin_box = QtWidgets.QSpinBox(self)
        spin_box.move(200, 200)

        # 设置按钮标志
        spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus)
        # spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)

        # 设置边框
        spin_box.setFrame(False)  # 不显示外边框

        # 设置只读模式
        spin_box.setReadOnly(True)  # 启用只读模式


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
