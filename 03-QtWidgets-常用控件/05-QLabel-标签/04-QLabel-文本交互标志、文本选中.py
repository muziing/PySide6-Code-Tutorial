import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

"""
QLabel 文本交互标志、选中


QLabel可以设置不同的文本交互标志，以控制用户交互
.setTextInteractionFlags(flags: Qt.TextInteractionFlags)    设置文本交互标志，具体见下方Qt.TextInteractionFlags
.textInteractionFlags() -> Qt.TextInteractionFlags          获取文本交互标志

Qt.TextInteractionFlags枚举值指定显示文本的控件对用户输入的反应方式
https://doc.qt.io/qt-6/qt.html#TextInteractionFlag-enum
 - Qt.NoTextInteraction              不能与文本进行交互
 - Qt.TextSelectableByMouse          可以使用鼠标选择文本，并用上下文菜单或标准键盘快捷键复制到剪贴板
 - Qt.TextSelectableByKeyboard       可以用键盘上的光标键选择文本，会显示一个文本光标
 - Qt.LinksAccessibleByMouse         链接高亮显示，并可用鼠标激活
 - Qt.LinksAccessibleByKeyboard      链接可以使用Tab键获得焦点，并通过Enter键激活
 - Qt.TextEditable                   文本完全可编辑
 - Qt.TextEditorInteraction          文本编辑器的默认值
 - Qt.TextBrowserInteraction         QTextBrowser的默认值

QLabel提供了选中文本内容相关的方法
.setSelection(start: int, length: int)    选中从start起长度length的文本
.selectedText() -> str                    返回选中的字符
.hasSelectedText() -> bool                返回是否有文本被选中
.selectionStart() -> int                  返回选择起始位置
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLabel-文本交互标志、文本选中")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.label_1 = QtWidgets.QLabel("不能与文本进行交互", self)
        self.label_2 = QtWidgets.QLabel("可用鼠标选择", self)
        self.label_3 = QtWidgets.QLabel(
            "<a href='https://doc.qt.io/qt-6/qlabel.html#textInteractionFlags-prop'>链接可激活</a>",
            self,
        )
        self.label_3.setOpenExternalLinks(True)
        self.label_4 = QtWidgets.QLabel("文本完全可编辑", self)

        self.label_1.move(320, 180)
        self.label_2.move(320, 220)
        self.label_3.move(320, 260)
        self.label_4.move(320, 300)

    def test_01(self) -> None:
        """测试文本交互标志"""
        self.label_1.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_2.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_3.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.LinksAccessibleByKeyboard
        )
        self.label_4.setTextInteractionFlags(Qt.TextEditable)

        print(self.label_2.textInteractionFlags() == Qt.TextSelectableByMouse)

    def test_02(self) -> None:
        """测试文本选中"""
        self.label_2.setSelection(0, 2)
        if self.label_2.hasSelectedText():
            print(self.label_2.selectedText())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
