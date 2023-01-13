"""
QLineEdit Action 案例
单行文本编辑器可以在行首或行尾添加自定义的行为
本案例为在编辑器尾部添加一个输入密码时的明文/掩码切换按钮

.addAction(action: QAction, position: QLineEdit.ActionPosition)
.addAction(icon: QIcon, position: QLineEdit.ActionPosition) -> QAction

QLineEdit.ActionPosition枚举值具体有以下两种取值：
QLineEdit.LeadingPosition      若布局从左至右则将行为添加至最左侧，反之则添加至最右侧
QLineEdit.TrailingPosition     若布局从左至右则将行为添加至最右侧，反之则添加至最左侧
"""

import sys

from PySide6 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-案例")
        self.resize(500, 300)
        self.setup()

    def setup(self) -> None:
        """设置界面与功能"""

        line_edit = QtWidgets.QLineEdit(self)
        line_edit.resize(300, 30)
        line_edit.move(100, 50)
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        eye_icon = QtGui.QIcon("../../Resources/Icons/FlatIcon-regular-rounded/eye.png")
        eye_crossed_icon = QtGui.QIcon(
            "../../Resources/Icons/FlatIcon-regular-rounded/eye-crossed.png"
        )

        # 创建行为，并将其触发连接到对应的功能槽函数
        action = QtGui.QAction(line_edit)
        action.setIcon(eye_crossed_icon)

        @QtCore.Slot()
        def switch():
            """切换明文/密码的槽函数"""
            if line_edit.echoMode() == QtWidgets.QLineEdit.EchoMode.Password:
                line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
                action.setIcon(eye_icon)
            else:
                line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
                action.setIcon(eye_crossed_icon)

        action.triggered.connect(switch)  # type: ignore

        # 添加行为
        line_edit.addAction(action, QtWidgets.QLineEdit.ActionPosition.TrailingPosition)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
