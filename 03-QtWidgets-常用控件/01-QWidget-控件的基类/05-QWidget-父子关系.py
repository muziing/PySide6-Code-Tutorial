import sys
from pprint import pprint

from PySide6 import QtGui, QtWidgets

"""
QWidget 提供了多种API来获取（访问）其父子控件

.setParent()       指定本控件的父控件
.parentWidget()    获取父控件
.children()        获取所有子控件，返回一个列表
.childAt()         获取在指定坐标的子控件
.childrenRect()    所有子控件（被隐藏的除外）构成的矩形
.childrenRegion()  所有子控件（被隐藏的除外）构成的范围
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget-父子关系")
        self.resize(400, 300)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.button = QtWidgets.QPushButton("点击我！", self)
        self.button.clicked.connect(lambda: print("按钮被点击了"))  # type: ignore
        self.button.move(50, 200)
        self.label_1 = QtWidgets.QLabel("PySide", self)
        self.label_1.move(150, 50)
        self.label_2 = QtWidgets.QLabel()  # 创建时未指定父控件
        self.label_2.setPixmap(QtGui.QPixmap("../../Resources/Icons/Python_128px.png"))
        self.label_2.setParent(self)  # 指定父控件

    def test_01(self) -> None:
        """测试访问子控件功能"""
        pprint(self.children())  # 打印所有子控件，以列表返回，顺序同添加顺序

        # 获取处于制定坐标的子控件
        # 注意：若该坐标无子控件则返回None、似乎对布局管理器无效
        print(self.childAt(150, 55))

        # 以上方法返回的子控件都可以被操作
        self.childAt(150, 55).setStyleSheet("background-color: cyan;")

        print(self.childrenRect())  # 打印所有子控件（被隐藏的除外）构成的矩形
        print(self.childrenRegion())

    def test_02(self) -> None:
        """测试访问父控件功能"""
        print(self.label_2.parentWidget())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
