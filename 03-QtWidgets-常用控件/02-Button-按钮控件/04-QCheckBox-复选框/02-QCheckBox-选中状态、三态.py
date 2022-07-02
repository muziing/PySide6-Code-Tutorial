import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

"""
QCheckBox 选中状态、三态

.setTristate(y: bool = True)           设置是否开启三态，默认关闭
.isTristate() -> bool                  获取是否开启了三态
.setCheckState(state: Qt.CheckState)   设置选中状态
.checkState() -> Qt.CheckState         获取选中状态

Qt.CheckState具体有如下三种：
https://doc.qt.io/qt-6/qt.html#CheckState-enum
 - Qt.Unchecked            该项目未选中
 - Qt.PartiallyChecked     该项目被部分选中：如果选中了分层模型中的部分（而非全部）子项目，则该项目部分选中
 - Qt.Checked              该项目被选中

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QCheckBox-选中状态")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.cb_1 = QtWidgets.QCheckBox("复选框1", self)
        self.cb_1.move(320, 150)
        self.cb_2 = QtWidgets.QCheckBox("复选框2", self)
        self.cb_2.move(320, 180)
        self.cb_3 = QtWidgets.QCheckBox("复选框3", self)
        self.cb_3.move(320, 210)

    def test_01(self) -> None:
        """测试三态"""
        print(self.cb_1.isTristate())  # 默认不开启三态
        self.cb_2.setTristate(True)  # 开启三态
        self.cb_3.setTristate(True)  # 开启三态

    def test_02(self) -> None:
        """测试选中状态"""
        self.cb_1.setCheckState(Qt.Checked)

        @QtCore.Slot()
        def test_slot():
            print(self.cb_3.checkState())

        self.cb_3.clicked.connect(test_slot)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
