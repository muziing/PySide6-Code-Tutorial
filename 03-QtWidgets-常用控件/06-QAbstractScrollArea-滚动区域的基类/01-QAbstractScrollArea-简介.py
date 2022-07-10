import sys

from PySide6 import QtGui, QtWidgets

"""
QAbstractScrollArea 滚动区域的基类

滚动区域的低级抽象。该区域提供了称为viewport的中央控件，该区域的内容将在其中
滚动（即，内容的可见部分在viewport中呈现）。

官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QAbstractScrollArea.html
继承自QFrame
被QScrollArea、QTextEdit、QPlainTextEdit、QAbstractItemView等继承

"""


# Window继承自QScrollArea,由于没有父控件，则作为顶层窗口显示
class Window(QtWidgets.QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractScrollArea-滚动区域")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        image_label = QtWidgets.QLabel(self)
        # 图像尺寸大于窗口尺寸，无法直接显示全部内容
        image_label.setPixmap(QtGui.QPixmap("../../Resources/Images/Python-code.jpg"))
        self.setWidget(image_label)  # 设置viewport


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
