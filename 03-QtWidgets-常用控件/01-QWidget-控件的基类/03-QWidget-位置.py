import sys

from PySide6 import QtWidgets

"""
坐标系以「左上角」为原点，向右为x轴正方向，向下为y轴正方向

当QWidget为窗口时，设置/获取其相对桌面的位置（包含其框架）
当QWidget为子控件时，设置/获取其相对父控件的位置
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget 位置")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self) -> None:
        """测试"""
        self.test_01()
        self.test_02()

    def test_01(self) -> None:
        """测试设置位置功能"""
        self.move(200, 200)  # 距离屏幕左上角向右向下移动200像素
        self.label = QtWidgets.QLabel("只是一个Label标签", self)  # 创建一个标签子控件
        self.label.move(100, 200)  # 相对父控件（窗口）移动位置

        self.setGeometry(200, 200, 600, 400)  # 可以同时设置其位置与尺寸，计算像素时不包含框架

    def test_02(self) -> None:
        """测试获取位置功能"""
        print(self.x())
        print(self.y())
        print(self.pos())
        print(self.label.pos())  # 显示的是相对于父控件的位置
        print(self.geometry())  # 位置、大小


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
