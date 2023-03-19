import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

"""
QCheckBox 信号
QCheckBox除了继承父类QAbstractButton提供的信号，只有一个可用信号

QCheckBox.stateChanged -> int  选中状态改变时发射此信号，新的选中状态作为参数传出，见Qt.CheckState
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QCheckBox-信号")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()

    def setup_ui(self) -> None:
        """设置界面"""
        self.cb = QtWidgets.QCheckBox("PySide6", self)
        self.cb.move(320, 200)
        self.cb.setTristate(True)

    def test_01(self) -> None:
        """测试信号"""

        @QtCore.Slot(int)
        def test_slot(state: int) -> None:
            if state == Qt.Checked:
                print("复选框被选中了！")
            elif state == Qt.Unchecked:
                print("复选框被取消选中了！")
            elif state == Qt.PartiallyChecked:
                print("复选框被部分选中！")

        self.cb.stateChanged.connect(test_slot)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
