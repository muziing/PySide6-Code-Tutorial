import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

"""
QLabel 信号

QLabel的可用信号只有链接被悬停、链接被点击两种，具体如下

.linkActivated(link: str)    当用户点击链接时发射此信号，将链接作为参数传出
.linkHovered(link: str)      当用户的光标置于链接之上时发射此信号，将链接作为参数传出

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLabel-信号")
        self.resize(800, 600)
        self.label_1 = QtWidgets.QLabel(self)
        self.label_2 = QtWidgets.QLabel(self)
        self.setup_ui()
        self.test_01()

    def setup_ui(self) -> None:
        """设置界面"""
        label_1 = self.label_1
        label_1.move(320, 200)
        label_1.setText(
            "<a href='https://github.com/muziing/PySide6-Code-Tutorial'>PySide6 Code Tutorial</a>"
        )

        label_2 = self.label_2
        label_2.move(320, 240)
        label_2.setText("[muzing的博客](https://muzing.top)")
        label_2.setTextFormat(Qt.MarkdownText)

    def test_01(self) -> None:
        """测试QLabel信号"""
        self.label_1.linkHovered.connect(lambda val: print(val))  # type: ignore
        self.label_2.linkHovered.connect(lambda val: print(val))  # type: ignore

        self.label_1.linkActivated.connect(lambda val: print(val))  # type: ignore
        self.label_2.linkActivated.connect(lambda val: print(val))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
