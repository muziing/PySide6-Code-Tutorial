import sys

from PySide6 import QtWidgets

"""
QPlainTextEdit 占位文本、Tab控制

======================================= 换行方式 ==================================================
设置占位文本（如“请输入用户名”），当用户开始编辑输入时自动消失，用于提示用户输入

.setPlaceholderText(placeholderText: str)     设置占位文本
.placeholderText() -> str                     获取占位文本

======================================= Tab控制 ==================================================
当当前焦点在QPlainText上时，按下键盘Tab键的默认行为是输入一个制表符，
可以以像素为单位精细控制制表符距离，或将Tab键的功能设置为切换焦点控件

.setTabStopDistance(distance: float)          设置Tab制表符的距离，单位为像素
.tabStopDistance() -> float                   获取Tab制表符距离
.setTabChangesFocus(b: bool)                  设置Tab键是否切换焦点至其他控件
.tabChangesFocus() -> bool                    获取Tab键是否为焦点切换功能

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPlainTextEdit-占位文本、Tab功能")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.pte = QtWidgets.QPlainTextEdit(self)
        self.pte.resize(400, 400)
        self.pte.move(200, 100)
        le = QtWidgets.QLineEdit(self)
        le.move(500, 50)

    def test_01(self) -> None:
        """测试占位文本功能"""
        self.pte.setPlaceholderText("请在此处输入文本")  # 设置占位文本
        print(self.pte.placeholderText())  # 获取占位文本

    def test_02(self) -> None:
        """测试Tab键功能"""
        # 控制Tab制表符的距离，单位为像素，默认值为80
        self.pte.setTabStopDistance(200)
        print(self.pte.tabStopDistance())  # 获取当前设置的制表符距离

        # 将键盘Tab键功能设置为在控件间切换焦点，而不是在编辑器中输入制表符
        # self.pte.setTabChangesFocus(True)  # 启用该功能，pte加入焦点链
        # print(self.pte.tabChangesFocus())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
