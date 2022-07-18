import sys

from PySide6 import QtWidgets

"""
QLineEdit 单行文本编辑器

用户可以输入单行文本。适用于输入用户名等场景。
如需输入多行文本、富文本，请使用QTextEdit控件。
默认自动支持常见键盘操作，如移动光标、Home/End、复制粘贴等，详情参考文档

官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QLineEdit.html
继承自QWidget

构造函数中可以传入显示的文字、父控件
.__init__(self, arg__1: str, parent: Optional[QWidget] = None)
.__init__(self, parent: Optional[QWidget] = None)

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-单行文本编辑器")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        # 创建时传入初始文本
        # line_edit = QtWidgets.QLineEdit("单行文本编辑器", self)

        # 也可以创建时不具有文本
        line_edit = QtWidgets.QLineEdit(self)
        line_edit.move(100, 100)

        # 通过代码设置文本内容
        line_edit.setText("QLineEdit")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
