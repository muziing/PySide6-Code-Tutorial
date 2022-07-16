import sys

from PySide6 import QtCore, QtGui, QtWidgets

"""
QPlainTextEdit 文本字符格式
可以为某个段落设置文本字符格式，如字体、下划线等
本质上是调用了编辑器的光标的 QTextCursor.setCharFormat()等方法
关于QTextCharFormat的更多用法见QtGu目录下对应目录

.setCurrentCharFormat(format: QTextCharFormat)      设置在插入新文本时使用的字符格式，如果已经选中了字符则直接应用
.currentCharFormat() -> QTextCharFormat             返回插入新文本时使用的字符格式
.mergeCurrentCharFormat(modifier: QTextCharFormat)  将modifier中指定的属性合并至当前字符格式，如果已经选中了字符则直接应用

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPlainTextEdit-文本字符格式")
        self.resize(800, 600)
        self.setup_ui()
        self.char_format_test()

    def setup_ui(self) -> None:
        """设置界面"""
        self.pte = QtWidgets.QPlainTextEdit(self)
        self.pte.resize(500, 450)
        self.pte.move(100, 100)
        self.button_1 = QtWidgets.QPushButton("设置字符格式", self)
        self.button_1.move(630, 150)
        self.button_2 = QtWidgets.QPushButton("合并字符格式", self)
        self.button_2.move(630, 200)

    def char_format_test(self) -> None:
        """测试文本字符格式功能"""

        char_format_1 = QtGui.QTextCharFormat()  # 创建文本字符格式对象
        char_format_1.setFontUnderline(True)  # 设置文本下划线
        char_format_1.setUnderlineColor(QtGui.QColor(0, 128, 128))  # 设置下划线颜色
        char_format_1.setFontItalic(True)  # 设置斜体
        char_format_1.setFontWeight(60)  # 设置字重

        char_format_2 = QtGui.QTextCharFormat()
        char_format_2.setBackground(QtGui.QColor("cyan"))  # 设置背景颜色

        @QtCore.Slot()
        def test_set_char_format():
            """测试设置文本字符串格式"""
            self.pte.setCurrentCharFormat(char_format_1)  # 设置字符格式
            self.pte.setFocus()  # 让文本编辑器重新获得焦点
            print(self.pte.currentCharFormat())  # 获取字符格式

        @QtCore.Slot()
        def test_merge_chr_format():
            """测试合并文本字符串格式"""
            self.pte.mergeCurrentCharFormat(char_format_2)

        self.button_1.clicked.connect(test_set_char_format)  # type: ignore
        self.button_2.clicked.connect(test_merge_chr_format)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
