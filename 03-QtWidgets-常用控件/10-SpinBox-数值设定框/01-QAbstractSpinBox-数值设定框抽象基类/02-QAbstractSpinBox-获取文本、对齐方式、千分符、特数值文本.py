"""
QAbstractSpinBox 文本相关功能

=================================== 获取文本 ===================================
使用text()方法可以获取数值设定框中包含前后缀的完整文本

.text() -> str                         获取当前SpinBox中的完整文本

=================================== 文本对齐方式 ===================================
可以指定文本在LineEdit中的水平对齐方式，可选值为Qt.AlignLeft（默认）、Qt.AlignRight、Qt.AlignHCenter

.setAlignment(flag: Qt.Alignment)      设置文本对齐方式
.alignment() -> Qt.Alignment           获取文本对齐方式

==================================== 千分符 ===================================
可以指定开启组分隔符（千分符），默认值为不开启

.setGroupSeparatorShown(shown: bool)   设置是否展示千分符
.isGroupSeparatorShown() -> bool       返回千分符展示状态

=================================== 特数值文本 ===================================
可以设置特数值文本，当当前值为最小值时，将显示该特数值文本，而原先的非数值，表示此选择有特殊/默认含义

.setSpecialValueText(text: str)        设置特数值文本
.specialValueText() -> str             获取当前特数值文本，若未设置则返回空字符串
"""

import sys

from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractSpinBox-文本相关功能")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面与测试功能"""

        spin_box = QtWidgets.QSpinBox(self)
        spin_box.move(200, 200)
        spin_box.setRange(1000, 999999999)  # 设置允许输入的范围，便于展示千分符功能

        # =================================== 获取文本 ===================================
        btn = QtWidgets.QPushButton("获取文本", self)
        btn.move(220, 300)
        btn.clicked.connect(lambda: print(spin_box.text()))  # type: ignore

        # =================================== 文本对齐方式 ===================================
        spin_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)  # 更改为水平居中对齐，默认为左对齐

        # ==================================== 千分符 ===================================
        spin_box.setGroupSeparatorShown(True)  # 显示千分符

        # =================================== 特数值文本 ===================================
        # 当开启特数值文本后，最小值会显示该文本而非原本的数值
        # 可用于接收特殊或默认的用户输入 例如某个用于获取图像缩放比例的SpinBox可以设置“自动调整”的含义
        # spin_box.setSpecialValueText("Auto自动调整")  # 设置特数值文本


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
