"""
QLineEdit 显示模式
默认显示模式为正常，即用户输入什么就显示什么
也可以通过设置输入模式，使用户的输入被隐藏，常用于输入密码的场景
改变显示模式不会影响编辑器中真实存储的文字，仍可正常获取

.setEchoMode(QLineEdit.EchoMode)   设置显示模式
.echoMode() -> QLineEdit.EchoMode  获取显示模式

QLineEdit.EchoMode枚举值具体有如下4种：
https://doc.qt.io/qt-6/qlineedit.html#EchoMode-enum
QLineEdit.Normal              按字符输入时的形式显示。默认值。
QLineEdit.NoEcho              不显示任何内容。常见场景：密码的长度也需要被保护，例如Linux输入密码
QLineEdit.Password            显示时用平台决定的密码掩码字符替代真实输入的字符
QLineEdit.PasswordEchoOnEdit  当字符正在被编辑时显示，否则行为与Password相同()

.text() -> str                返回LineEdit内的文本，与显示模式无关
.displayText() -> str         返回LineEdit中显示的文本。例如Password模式下可能会获得"*******"
"""

import sys

from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-输入模式")
        self.resize(400, 300)
        self.setup_ui()
        self.test_echo_mode()

    def setup_ui(self) -> None:
        """设置界面"""

        label_1 = QtWidgets.QLabel("用户名")
        label_2 = QtWidgets.QLabel("密码")
        label_3 = QtWidgets.QLabel("编辑时可见的密码")
        label_4 = QtWidgets.QLabel("长度也保密的密码")

        self.line_edit_1 = QtWidgets.QLineEdit()
        self.line_edit_2 = QtWidgets.QLineEdit()
        self.line_edit_3 = QtWidgets.QLineEdit()
        self.line_edit_4 = QtWidgets.QLineEdit()

        self.button = QtWidgets.QPushButton("打印输入内容")

        # 使用布局管理器布局控件
        # 首次学习时可以略过本段代码
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(label_1, self.line_edit_1)
        form_layout.addRow(label_2, self.line_edit_2)
        form_layout.addRow(label_3, self.line_edit_3)
        form_layout.addRow(label_4, self.line_edit_4)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.button)

        self.setLayout(main_layout)

    def test_echo_mode(self) -> None:
        """测试显示模式功能"""
        self.line_edit_1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.line_edit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_edit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.line_edit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.NoEcho)

        @QtCore.Slot()
        def test_slot():
            """获取各编辑器的文本并打印到终端"""
            print(f"用户名为：{self.line_edit_1.text()}")
            print(f"密码为：{self.line_edit_2.text()}")
            print(f"编辑时可见的密码为：{self.line_edit_3.text()}")
            print(f"长度也保密的密码为：{self.line_edit_4.text()}")
            print(f"密码显示为：{self.line_edit_2.displayText()}")

        self.button.clicked.connect(test_slot)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
