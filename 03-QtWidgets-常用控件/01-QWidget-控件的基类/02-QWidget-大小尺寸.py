import sys

from PySide6 import QtWidgets

"""
QWidget 提供了丰富的尺寸设置功能，通过代码可以指定其尺寸、最大最小尺寸、获取当前尺寸等
默认行为：能完整显示其子控件的最小尺寸
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget 尺寸大小")
        self.setup_ui()

    def setup_ui(self) -> None:
        """测试功能"""
        self.test_01()
        self.test_02()
        self.test_03()

    def test_01(self) -> None:
        """测试设置尺寸功能"""
        # 设置尺寸
        self.resize(800, 600)  # 设置为指定尺寸，单位为像素

        # 最大最小尺寸
        # self.setMaximumSize(1000, 800)  # 限制最大尺寸，用户拖拽窗口能达到的最大大小
        # self.setMaximumWidth(1000)  # 亦可分别单独设置最大宽高
        # self.setMaximumHeight(800)
        # self.resize(1500, 1000)  # 即使再通过resize设置更大的尺寸，也无效

        # 固定尺寸
        # self.setFixedSize(500, 500)  # 设置为固定尺寸，用户不再可拖拽改变窗口尺寸
        # self.setFixedWidth(500)  # 也可以分别单独设置固定的宽高
        # self.setFixedHeight(500)

    def test_02(self) -> None:
        """测试大小自动调整功能"""
        # 注意首先将固定尺寸代码注释掉

        # 设置一个可以通过按钮增长的文本标签,初次阅读代码时本段可暂时忽略
        btn = QtWidgets.QPushButton("增长文本", self)
        btn.move(100, 300)
        label = QtWidgets.QLabel("muzing.top", self)
        label.move(0, 100)

        def test_slot():
            """测试用槽函数，增长label内文字"""
            new_content = label.text() + " muzing.top"
            label.setText(new_content)
            label.adjustSize()  # label的大小会根据其内容进行调整

            # ******************
            self.adjustSize()  # self的大小根据其子控件大小进行调整
            # ******************

        # 将按钮的点击信号与槽函数绑定，按钮按下则执行槽函数
        btn.clicked.connect(test_slot)  # type: ignore

    def test_03(self) -> None:
        """测试获取尺寸功能"""
        print(self.height())
        print(self.width())
        print(self.size())  # 返回QSize对象


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
