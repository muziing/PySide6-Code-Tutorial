import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

"""
QWidget 键盘输入焦点控制

只有当前获得焦点的控件才能与用户交互

每个控件都可以设置自己的焦点策略，即通过何种方式可以获取焦点
对于QPushButton、QTextEdit等控件的默认策略为StrongFocus，即可以通过键盘Tab键和鼠标点击两种方式获得焦点
对于QLabel等不需要与用户进行键盘输入交互的控件，焦点策略为NoFocus，不加入焦点链

https://doc.qt.io/qt-6/qwidget.html#setFocusProxy
.setFocusPolicy(policy: Qt.FocusPolicy)      设置焦点策略，详见下方Qt.FocusPolicy
.focusPolicy() -> Qt.FocusPolicy             返回该控件的焦点策略                               

Qt.FocusPolicy 具体分为如下数种：
https://doc.qt.io/qt-6/qt.html#FocusPolicy-enum
 - Qt.TabFocus         通过键盘Tab键获取焦点
 - Qt.ClickFocus       通过鼠标点击获取焦点
 - Qt.StrongFocus      通过键盘Tab或鼠标点击获取焦点
 - Qt.WheelFocus       在StrongFocus基础上，还支持鼠标滚轮滚动获取焦点
 - Qt.NoFocus          该控件不接受焦点，QLabel等不需要用户键盘操作的控件的默认值

Qt.WheelFocus 补充：若只有一个控件设置为此策略，则需要当前焦点在该控件的上/下一个焦点时才有效


焦点链默认顺序为子控件创建顺序，即按下键盘Tab键时会按子控件创建顺序依次切换焦点
.setTabOrder(fist: QWidget, second: QWidget) 将第二个控件从焦点链中移除，并放置到第一个控件之后

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QWidget-焦点控制-2")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.button = QtWidgets.QPushButton("测试按钮", self)
        self.button.move(200, 200)

        # 单行文本编辑器，当获得焦点时可以输入内容
        self.le = QtWidgets.QLineEdit(self)
        self.le.move(350, 100)

        # 下拉菜单，当获得焦点时可以用键盘方向键上下切换当前所选
        self.cbb = QtWidgets.QComboBox(self)
        self.cbb.addItem("选项1")
        self.cbb.addItem("选项2")
        self.cbb.move(500, 100)

        # 纯文本编辑器，当获得焦点时可以输入内容
        self.pte = QtWidgets.QPlainTextEdit(self)
        self.pte.setTabChangesFocus(True)  # 将纯文本编辑器中按下Tab键功能设置为切换焦点
        self.pte.move(350, 150)

        self.label = QtWidgets.QLabel("标签控件默认焦点策略为NoFocus", self)
        self.label.move(350, 360)

    def test_01(self):
        """测试焦点策略"""
        # 对于QPlainTextEdit纯文本编辑器，默认策略为Qt.StrongFocus
        # 分别在如下设置中尝试不同的策略，注释掉其他行

        # self.pte.setFocusPolicy(Qt.TabFocus)  # 只能通过键盘Tab键获取焦点
        # self.pte.setFocusPolicy(Qt.ClickFocus)  # 只能通过鼠标点击获取焦点
        self.pte.setFocusPolicy(Qt.StrongFocus)  # 可以通过以上两种方式获取焦点
        # self.pte.setFocusPolicy(Qt.WheelFocus)  # 还可以通过鼠标滚轮滚动获取焦点
        # self.pte.setFocusPolicy(Qt.NoFocus)  # 无法获得焦点，用户无法使用键盘对该控件操作

        # 强行令标签控件也可以获得焦点，无视觉效果，但在连续使用Tab切换焦点时可以感知到已经被加入焦点链
        self.label.setFocusPolicy(Qt.StrongFocus)

    def test_02(self):
        """测试调整焦点链顺序"""
        self.setTabOrder(self.pte, self.cbb)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
