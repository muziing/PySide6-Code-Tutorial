import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("控件测试模板")  # 设置窗口标题
        self.resize(800, 600)  # 设置窗口大小
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        # 创建一个按钮控件，其父控件为MyWidget
        button = QtWidgets.QPushButton("点击我！", self)
        button.move(300, 300)  # 移动按钮控件的位置


if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # 创建APP
    window = MyWidget()  # 实例化一个MyWidget类对象
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 正常退出APP
