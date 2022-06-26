import sys

from PySide6 import QtGui, QtWidgets

"""
QLabel 内边距、位图缩放

QLabel还可以调整内边距、启用内容缩放，以更细致地调节显示效果

.setMargin(int)                设置内边距（框架的最内部像素和内容的最外部像素之间的距离）
.margin() -> int               获取内边距，默认值为0
.setScaledContents(bool)       设置是否启用缩放
.hasScaledContents() -> bool   返回是否启用了缩放
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLabel-内容边距、缩放")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面，测试功能"""
        # 内边距
        label_1 = QtWidgets.QLabel("PySide6", self)
        label_1.move(340, 100)
        label_1.setStyleSheet("background-color: cyan;")
        label_1.setMargin(20)  # 设置边距
        print(label_1.margin())  # 获取边距

        # 启用缩放
        label_2 = QtWidgets.QLabel(self)
        label_2.resize(50, 50)
        label_2.move(350, 200)
        label_2.setPixmap(QtGui.QPixmap("../../Resources/Icons/OS_Ubuntu_128px.ico"))
        # 该位图为128像素宽高，label2仅有50像素，如不缩放，则只能显示位图的一部分
        label_2.setScaledContents(True)  # 启用内容缩放
        print(label_2.hasScaledContents())  # 获取是否开启了缩放


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
