import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

"""
QLabel 文本格式、链接

=================================== 文本格式 ===================================

QLabel可以将其文本字符串解析为纯文本、HTML富文本、Markdown文本

.setTextFormat(Qt.TextFormat)    设置文本格式，默认为Qt.AutoText
.textFormat() -> Qt.TextFormat   获取文本格式

Qt.TextFormat 具体分为四种：
https://doc.qt.io/qt-6/qt.html#TextFormat-enum
 - Qt.PlaintText        将文本字符串解析为纯文本
 - Qt.RichText          将文本字符串解析为富文本
 - Qt.AutoText          自动识别为纯文本或富文本
 - Qt.MarkdownText      将文本字符串解析为Markdown格式的文本


=================================== 链接 ===================================

对于QLabel中的链接，默认行为为发射linkActivated()信号，但也可以指定使用
QDesktopServices::openUrl() 在默认浏览器中打开链接。
注意textInteractionFlags应该设置为LinksAccessibleByMouse或LinksAccessibleByKeyboard。

.setOpenExternalLinks(open: bool)
.openExternalLinks() -> bool

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLabel-文本格式、链接")
        self.resize(800, 600)
        self.label_1 = QtWidgets.QLabel(self)
        self.label_2 = QtWidgets.QLabel(self)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        label_1 = self.label_1
        label_1.move(320, 200)
        label_1.setText(
            "<a href='https://github.com/muziing/PySide6-Code-Tutorial'>PySide6 Code Tutorial</a>"
        )

        label_2 = self.label_2
        label_2.move(320, 230)
        label_2.setText("**Markdown**")

    def test_01(self) -> None:
        """测试文本格式功能"""
        print(self.label_1.textFormat())  # 默认为 Qt.AutoText，所以可以识别富文本
        self.label_2.setTextFormat(Qt.MarkdownText)  # 设置为Qt.MarkdownText后即可被正确解析

    def test_02(self) -> None:
        """测试链接功能"""
        # 链接被点击时的默认行为是发射信号
        self.label_1.linkActivated.connect(lambda val: print(val))  # type: ignore

        # 也可以指定为使用默认浏览器打开，而不发射信号
        # self.label_1.setOpenExternalLinks(True)  # 点击链接则使用默认浏览器打开，不再发射信号


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
