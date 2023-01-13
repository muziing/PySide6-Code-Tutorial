"""
QPlainTextEdit 换行方式、只读

======================================= 换行方式 ==================================================
QPlainTextEdit 可以精细控制长文本在其中编辑时的换行方式

可以控制是否开启自动换行
.setLineWrapMode(mode: QPlainTextEdit.lineWrapMode)
.lineWrapMode() -> QPlainTextEdit.lineWrapMode

QPlainTextEdit.lineWrapMode枚举值具体包括以下：
https://doc.qt.io/qt-6/qplaintextedit.html#LineWrapMode-enum
QPlainTextEdit.WidgetWidth    按控件宽度换行（默认行为，即自动换行）
QPlainTextEdit.NoWrap         关闭自动换行


还可以控制单词换行方式，即在处理英文文本时，是否允许在单词中间换行（打断单词）
.setWordWrapMode(policy: QTextOption.WrapMode)   设置单词换行方式
.wordWrapMode() -> QTextOption.WrapMode          获取单词换行方式


QTextOption.WrapMode枚举值具体分为如下数种，控制文本在文档中如何换行
https://doc.qt.io/qt-6/qtextoption.html#WrapMode-enum
QTextOption.NoWrap                            文本永不换行
QTextOption.WordWrap                          文本在单词边界换行
QTextOption.ManualWrap                        与QTextOption.NoWrap相同
QTextOption.WrapAnywhere                      文本可以在一行的任意位置换行，甚至打断单词
QTextOption.WrapAtWordBoundaryOrAnywhere      尽可能在单词边界处换行，否则在任意位置换行


======================================= 只读 =====================================================
当启用只读功能后，用户只能选中文本，而不能编辑文本。
只读与不可用（QWidget.setEnabled(False)）的区别在于前者的文本仍可被选中，而后者的无法被选中。
只读模式下，有部分键鼠绑定可用，如键盘方向键控制移动等，详细请参考：
https://doc.qt.io/qt-6/qplaintextedit.html#read-only-key-bindings

.setReadOnly(ro: bool)    设置只读状态
.isReadOnly() -> bool     返回是否开启了只读
"""

import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QTextOption

long_text = """Gatsby believed in the green light, the orgastic future that year by year recedes before us. \
It eluded us then, but that's no matter--tomorrow we will run faster, stretch out our arms farther... \
And one fine morning----\nSo we beat on, boats against the current, borne back ceaselessly into the past."""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPlainTextEdit-功能测试")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.pte = QtWidgets.QPlainTextEdit(self)
        self.pte.resize(400, 400)
        self.pte.move(200, 100)
        self.pte.insertPlainText(long_text)

    def test_01(self) -> None:
        """测试自动换行功能"""

        # 设置换行模式
        self.pte.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth)  # 自动换行（默认值）
        # self.pte.setLineWrapMode(QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap)  # 关闭自动换行
        print(self.pte.lineWrapMode())  # 获取换行模式

        # 设置单词换行方式
        # self.pte.setWordWrapMode(QTextOption.WrapMode.NoWrap)  # 永不换行
        # self.pte.setWordWrapMode(QTextOption.WrapMode.WordWrap)  # 在单词间换行
        # self.pte.setWordWrapMode(QTextOption.WrapMode.ManualWrap)  # 同NoWrap
        # self.pte.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)  # 在任意位置换行，可能打断单词
        self.pte.setWordWrapMode(
            QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere
        )  # 尽可能单词间换行，否则任意换行
        print(self.pte.wordWrapMode())  # 获取单词换行方式

    def test_02(self) -> None:
        """测试只读模式功能"""

        self.pte.setReadOnly(True)  # 启用只读模式
        # self.pte.setReadOnly(False)  # 关闭只读模式
        print(self.pte.isReadOnly())  # 获取只读状态

        # self.setEnabled(False)  # 如果设置不可用状态，则文本也无法被选中


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
