import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

"""
QLineEdit 文本边距、对齐方式、边框

=========================== 文本边距 ============================
可以设置文字与编辑器边界间的内边距，设置方法有两种重载，传入
QMargins 或「左上右下」四个 int 均可

.setTextMargins(left: int, top: int, right: int, bottom: int)
.setTextMargins(margins: QMargins)      设置控件的文本边距
.textMargins() -> QMargins              返回控件的文本边距

=========================== 对齐方式 ============================
文字区域的矩形布置在整个单行编辑器区域中时，可以设置对齐方式
Qt.Alignment 枚举值的具体类型参见本项目00-01-Qt命名空间

.setAlignment(flag: Qt.Alignment)
.alignment() -> Qt.Alignment

============================ 边框 =============================
默认情况下，line edit会绘制一个边框，也可以通过代码设置取消

.setFrame(yes: bool)   设置边框。默认值为True
.hasFrame() -> bool    返回是否具有边框

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-文本边距、对齐方式、边框")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()

    def setup_ui(self) -> None:
        """设置界面"""
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.resize(300, 50)
        self.line_edit.move(250, 50)

    def test_01(self) -> None:
        """测试文本编辑器功能"""

        # 设置文本对齐方式
        self.line_edit.setAlignment(Qt.AlignRight | Qt.AlignTop)

        # 设置文本边距
        self.line_edit.setTextMargins(50, 0, 0, 0)
        # 设置边距后不便于观察对齐方式，最好注释掉其中之一

        # 设置边框
        self.line_edit.setFrame(False)  # 取消了默认存在的边框
        self.line_edit.setText("Line edit without frame.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
