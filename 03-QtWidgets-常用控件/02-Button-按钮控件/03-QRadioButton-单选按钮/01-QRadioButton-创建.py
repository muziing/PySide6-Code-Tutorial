import sys

from PySide6 import QtGui, QtWidgets

"""
QRadioButton 单选按钮
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QRadioButton.html

默认开启排他性，即在一个按钮组中，只能同时有一个单选按钮被选中
属于同一个父控件的多个单选按钮，有排他性

QRadioButton(text: str, parent: QWidget=None)
QRadioButton(parent: QWidget=None)
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QRadioButton-创建")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        radio_button_1 = QtWidgets.QRadioButton("男", self)
        radio_button_2 = QtWidgets.QRadioButton("女", self)
        radio_button_1.setIcon(
            QtGui.QIcon("../../../Resources/Icons/FlatIcon-regular-rounded/mars.png")
        )
        radio_button_2.setIcon(
            QtGui.QIcon("../../../Resources/Icons/FlatIcon-regular-rounded/venus.png")
        )
        radio_button_1.setShortcut("Alt+M")  # 设置快捷键
        radio_button_2.setShortcut("Alt+F")
        radio_button_1.move(350, 200)
        radio_button_2.move(350, 260)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
