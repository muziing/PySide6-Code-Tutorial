import sys

from PySide6 import QtWidgets

"""
QLineEdit-长度限制、占位文本、只读

=========================== 长度限制 ============================
单行文本编辑器可以限制用户输入的最大字符长度。
如果长度超出限制则会被在max处截断。
如果设置了掩码（见本目录其他文档），则长度由掩码限制

.setMaxLength(length: int)      设置文本最大长度，默认值为32767
.maxLength() -> int             返回最大长度限制

=========================== 占位文本 ============================
可以在用户未输入任何内容时设置一个占位文本，起到提示作用，
例如“在此处输入用户名”。当用户开始编辑时消失。

.setPlaceholderText(text: str)  设置占位文本
.placeholderText() -> str       返回占位文本

============================ 只读 =============================
可以开启只读模式，用户无法编辑其中的内容。与不可用（QWidget.setEnabled(False)）的区别在于，
用户仍然可以复制其中的文本到剪切板、拖动文本等。
在只读模式下，不会显示光标。

.setReadOnly(yes: bool)         设置是否开启只读模式，默认为False
.isReadOnly() -> bool           获取只读状态

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-长度限制、占位文本、只读")
        self.resize(800, 600)
        self.setup_ui()

        # 注意test_01与test_02互斥，测试其中之一时注释掉另一个
        # self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.resize(300, 30)
        self.line_edit.move(250, 50)

    def test_01(self) -> None:
        """测试功能"""

        # 限制用户输入最大长度
        self.line_edit.setMaxLength(20)
        print(self.line_edit.maxLength())  # 获取最大长度

        # 设置占位文本
        self.line_edit.setPlaceholderText("请输入用户名")

    def test_02(self) -> None:
        """测试只读模式"""

        self.line_edit.setText("https://github.com/muziing/PySide6-Code-Tutorial")
        self.line_edit.setReadOnly(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
