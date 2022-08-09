import sys

from PySide6 import QtWidgets

"""
QLineEdit  自动补全（完成器）

单行文本编辑器可以设置一个完成器（QCompleter），以实现自动补全功能
当用户输入与完成器中的某项相近时，会自动在编辑器下方弹出combobox供用户选择
注意与验证器或补码共同使用时，自动填充项需要满足验证器/掩码要求

QCompleter官方文档：https://doc.qt.io/qt-6/qcompleter.html

.setCompleter(c: QCompleter)    设置完成器
.completer() -> QCompleter      获取完成器

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-自动补全")
        self.resize(800, 600)
        self.setup_ui()
        self.test_completer()

    def setup_ui(self) -> None:
        """设置界面"""

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("测试自动补全功能")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def test_completer(self) -> None:
        """测试完成器功能"""

        # 创建完成器对象
        completer = QtWidgets.QCompleter(["PyQt", "PySide", "PyQt6", "PySide6"], self.line_edit)
        # 为line_edit设置完成器
        self.line_edit.setCompleter(completer)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
