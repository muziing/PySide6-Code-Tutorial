import sys

from PySide6 import QtWidgets

"""
QCheckBox  复选框
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QCheckBox.html
继承自QAbstractButton

复选框一般有两种选中状态（选中/未选中），有时则是三种（全部选中/部分选中/未选中）
用于让用户勾选/取消勾选某些选项等
复选框默认没有排他性，也可以通过QButtonGroup分组后用setAutoExclusive()方法开启

.__init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None)
.__init__(self, text: str, parent: Optional[PySide6.QtWidgets.QWidget] = None)  创建时即设置文字
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QCheckBox-创建")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        cb_1 = QtWidgets.QCheckBox("早餐", self)
        cb_1.move(320, 200)
        cb_2 = QtWidgets.QCheckBox(self)
        cb_2.setText("午餐")
        cb_2.move(320, 240)
        cb_3 = QtWidgets.QCheckBox()
        cb_3.setParent(self)
        cb_3.setText("晚餐")
        cb_3.move(320, 280)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
