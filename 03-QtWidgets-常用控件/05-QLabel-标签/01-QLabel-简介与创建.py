import sys

from PySide6 import QtWidgets

"""
QLabel 标签控件

标签控件用于在界面上显示文字、图像等
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLabel.html
继承自 QFrame

有两种构造函数，可以传入文本、父控件、Qt.WindowFlags(一般不用)三个参数：
__init__(self, parent: Optional[QtWidgets.QWidget] = None, f: Qt.WindowFlags = Default(Qt.WindowFlags))
__init__(self, text: str, parent: Optional[QtWidgets.QWidget] = None, f: Qt.WindowFlags = Default(Qt.WindowFlags))

QLabel的大小会根据其内容自动调整，也可以手动指定

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLabel-创建")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        label = QtWidgets.QLabel("PySide6", self)  # 创建时即设置了标签文本与父对象
        label.move(350, 200)

        # 也可以创建空白标签，随后设置父控件与文字
        label_2 = QtWidgets.QLabel()
        label_2.setParent(self)
        label_2.setText("QLabel 标签控件")
        label_2.move(350, 240)

        # 将label2设置显示背景颜色，以直观感受创建时其尺寸大小随内容自动调整
        label_2.setStyleSheet("background-color: cyan;")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
