import sys

from PySide6 import QtWidgets

"""
QWidget 键盘输入焦点控制

只有当前获得焦点的控件才能与用户交互
Qt提供了强大的焦点控制的API
键盘Tab键可以在控件间移动焦点，也可以用代码指定子控件获取焦点的先后顺序

对本控件的焦点的控制：
https://doc.qt.io/qt-6/qwidget.html#setFocus
.hasFocus() -> bool                          返回此控件（或其焦点代理）是否具有键盘输入焦点
.setFocus()                                  槽函数，若其父控件为活动窗口，则为此控件（或其焦点代理）设置焦点
.setFocus(reason: Qt.FocusReason)            Qt.FocusReason 详见下文
.clearFocus()                                移除控件的焦点

对子控件的焦点的控制：
https://doc.qt.io/qt-6/qwidget.html#focusNextPrevChild
.focusNextChild() -> bool
.focusPreviousChild() -> bool
.focusNextPrevChild(next: bool) -> bool      上两种方法的结合，当next为True时向前搜索，否则向后搜索
.focusWidget() -> QWidget


Qt.FocusReason 具体分为如下数种：
https://doc.qt.io/qt-6/qt.html#FocusReason-enum
 - Qt.MouseFocusReason           鼠标活动导致
 - Qt.TabFocusReason             按下了Tab键
 - Qt.BacktabFocusReason         Backtab导致，例如按下Shift+Tab键
 - Qt.ActiveWindowFocusReason    窗口系统使该窗口处于活动或非活动状态
 - Qt.PopupFocusReason           应用程序打开/关闭一个弹出窗口，该弹出窗口抓取/释放键盘焦点
 - Qt.ShortcutFocusReason        用户输入了一个标签的伙伴快捷键（参阅QLabel.buddy）
 - Qt.MenuBarFocusReason         菜单栏获得了焦点
 - Qt.OtherFocusReason           其他原因

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QWidget-焦点控制")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()

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

    def test_01(self):
        """测试设置焦点功能"""
        # self.button.clicked.connect(self.pte.setFocus)  # type: ignore
        self.button.clicked.connect(self.focusNextChild)  # type: ignore
        self.button.clicked.connect(lambda: print(self.button.hasFocus()))  # type: ignore
        self.button.clicked.connect(lambda: print(self.le.hasFocus()))  # type: ignore
        self.button.clicked.connect(lambda: print(self.focusWidget()))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
