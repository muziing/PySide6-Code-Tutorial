import sys

from PySide6 import QtWidgets

"""
QComboBox 组合下拉框
QComboBox控件是按钮和弹出式列表的结合，用于在很小的控件内为用户提供多个选项
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QComboBox.html
继承自QWidget

只有一种构造函数，可选参数为父控件
.__init__(self, parent: Optional[QWidget] = None)
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("空白测试模板")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 实例化一个QComboBox,指定父控件为self
        cbb = QtWidgets.QComboBox(self)
        cbb.move(300, 100)

        # 添加条目
        cbb.addItem("PySide 6")
        cbb.addItem("PyQt 6")
        cbb.addItem("PyQt 5")
        cbb.addItem("PySide 2")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
