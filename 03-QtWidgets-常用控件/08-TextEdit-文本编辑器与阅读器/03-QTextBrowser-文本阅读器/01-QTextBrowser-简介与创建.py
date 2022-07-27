import sys

from PySide6 import QtWidgets

"""
QTextBrowser 文本浏览器/阅读器
具有超文本导航的富文本浏览器
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTextBrowser.html
继承自QTextEdit

只有一种构造函数，可以指定父对象
.__init__(self, parent: Optional[QWidget] = None)
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QTextBrowser")
        self.resize(800, 600)
        self.text = (
            "Gatsby believed in the green light, the orgastic future that year by year recedes before us. "
            "It eluded us then, but that's no matter--tomorrow we will run faster, stretch out our arms farther. . . . "
            "And one fine morning----\nSo we beat on, boats against the current, borne back ceaselessly into the past."
        )
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建文本阅读器
        text_browser = QtWidgets.QTextBrowser(self)
        text_browser.setText(self.text)
        text_browser.resize(300, 200)
        text_browser.move(200, 200)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
