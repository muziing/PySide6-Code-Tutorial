import sys

from PySide6 import QtWidgets

"""
QAbstractButton 自动排他功能
该功能主要用于单选按钮：一组单选按钮都有排他性，即一次只能选中其中一项，选中新的项会导致之前选择的项取消
除QRadioButton子类外，该功能默认关闭
更多信息参见本项目 QRadioButton 目录

.setAutoExclusive(bool)    设置是否开启自动排他性，默认为false
.autoExclusive() -> bool   获取按钮是否开启了自动排他性
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractButton-排他性")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面与测试功能"""
        button_1 = QtWidgets.QCheckBox("按钮1", self)
        button_2 = QtWidgets.QCheckBox("按钮2", self)
        button_3 = QtWidgets.QCheckBox("按钮3", self)
        button_4 = QtWidgets.QCheckBox("按钮4", self)
        button_1.move(380, 100)
        button_2.move(380, 150)
        button_3.move(380, 200)
        button_4.move(380, 250)

        # QCheckBox默认不开启排他性，可以同时选中多个
        # 下面手动开启按钮1～3的排他性，这3个按钮中只能同时选中1个
        button_1.setAutoExclusive(True)
        button_2.setAutoExclusive(True)
        button_3.setAutoExclusive(True)

        print(button_4.autoExclusive())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
