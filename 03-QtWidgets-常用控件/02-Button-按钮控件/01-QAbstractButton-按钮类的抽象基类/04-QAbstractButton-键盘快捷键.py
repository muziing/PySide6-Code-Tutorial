import sys

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

"""
QAbstractButton 键盘快捷键
按钮控件可以设置键盘快捷键，用户在键盘上按下快捷键时即触发按钮点击动作

建议阅读：https://doc.qt.io/qt-6/qkeysequence.html
关于 QKeySequence 更多内容，请参考本项目QtGui目录下的QKeySequence目录

.setShortcut(QKeySequence)    为按钮设置键盘快捷键
.shortcut() -> QKeySequence   获取按钮的键盘快捷键
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractButton-键盘快捷键")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 快速添加快捷键，按键为 Alt + 紧贴'&'符号后面的字母
        button_1 = QtWidgets.QPushButton("&button1", self)  # 使用 Alt+B 即可触发按钮1

        button_2 = QtWidgets.QPushButton("button2", self)
        button_1.move(350, 200)
        button_2.move(350, 300)
        button_1.clicked.connect(lambda: print("按钮1 被点击了！"))  # type: ignore
        button_2.clicked.connect(lambda: print("按钮2 被点击了！"))  # type: ignore

        button_2.setShortcut(QtGui.QKeySequence(Qt.CTRL + Qt.Key_A))  # 添加 Ctrl+A 的键盘快捷键
        print(button_2.shortcut())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
