"""
QFrame 是具有边框的控件的基类
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFrame.html
继承自QtWidget
例如QMenu的“浮起”、QProgressBar的“下沉”、QLabel的“扁平”视觉效果都是来自QFrame

风格与线宽纵览图：https://doc.qt.io/qt-6/images/frames.png

构造函数中可以传入父控件与WindowFlags（见本项目05-03-01）
.__init__(self, parent: Optional[QWidget] = None, f: Qt.WindowFlags = Default(Qt.WindowFlags))
"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QFrame")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        frame = QtWidgets.QFrame(self)
        frame.setStyleSheet("background-color: cyan;")
        frame.move(200, 200)

        # 设置风格与线宽
        frame.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Sunken)
        frame.setLineWidth(3)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
