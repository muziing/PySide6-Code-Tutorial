import sys

from PySide6 import QtGui, QtWidgets

"""
QScrollArea 滚动区域
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QScrollArea.html
滚动区域类为另一个控件提供了可以滚动查看的视图
继承自QAbstractScrollArea

构造函数中只有一个可选的参数：父控件
.__init__(self, parent: Optional[QWidget] = None)
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QScrollArea-滚动区域")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        # 创建滚动区域
        scroll_area = QtWidgets.QScrollArea(self)

        image_label = QtWidgets.QLabel(scroll_area)
        image_label.setPixmap(QtGui.QPixmap("../../Resources/Images/Python-code.jpg"))

        # 将图像标签设置为滚动区域的视图控件
        scroll_area.setWidget(image_label)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
