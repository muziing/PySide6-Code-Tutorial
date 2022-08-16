import sys

from PySide6 import QtWidgets

"""
QFontComboBox 字体选择下拉框
以下拉框的形式让用户选择字体家族（font family）
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFontComboBox.html
继承自QComboBox

关于QFont字体的更多信息，参考本项目QtGui下的QFont条目

只有一种构造函数，可选传入父控件
.__init__(self, parent: Optional[QWidget] = None)
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QFontComboBox")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建一个字体选择下拉框
        fcb = QtWidgets.QFontComboBox()

        # 创建示例文本并连接信号，当用户选择字体改变时，对应改变示例文本的字体
        text_label = QtWidgets.QLabel("我能吞下玻璃而不伤身体\nThe quick brown fox jumps over the lazy dog.")
        fcb.currentFontChanged.connect(text_label.setFont)  # type: ignore

        # 使用布局管理器布局界面
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(fcb)
        layout.addWidget(text_label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
