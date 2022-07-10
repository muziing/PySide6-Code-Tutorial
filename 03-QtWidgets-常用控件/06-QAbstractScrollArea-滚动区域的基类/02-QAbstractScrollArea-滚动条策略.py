import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

"""
QAbstractScrollArea 滚动条显示策略

滚动条显示策略由 Qt.ScrollBarPolicy 列出，具体如下：
https://doc.qt.io/qt-6/qt.html#ScrollBarPolicy-enum
Qt.ScrollBarAsNeeded      只有当内容太大而无法容纳时，QAbstractScrollArea 才显示滚动条。此为默认值
Qt.ScrollBarAlwaysOff     QAbstractScrollArea 永不显示滚动条
Qt.ScrollBarAlwaysOn      QAbstractScrollArea 总显示一个滚动条。此属性在具有瞬态滚动条的操作系统上被忽略

即使不显示滚动条，也仍可通过键盘方向键、鼠标滚轮等控制滚动区域滚动

.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy)     设置水平滚动条策略
.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy)       设置垂直滚动条策略
.horizontalScrollBarPolicy() -> Qt.ScrollBarPolicy    获取水平滚动条策略
.verticalScrollBarPolicy() -> Qt.ScrollBarPolicy      获取垂直滚动条策略
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("空白测试模板")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()

    def setup_ui(self) -> None:
        """设置界面"""
        self.pte = QtWidgets.QPlainTextEdit(self)
        self.pte.resize(400, 250)

        button_1 = QtWidgets.QPushButton("增加文本", self)
        button_1.move(500, 80)

        @QtCore.Slot()
        def append_text():
            """按钮的槽函数，用于为文本编辑器添加行"""
            self.pte.appendPlainText("PySide6\nPySide6")
            # 逐渐增加文本至编辑器无法全面显示时，体现滚动条策略的效果

        button_1.clicked.connect(append_text)  # type: ignore

    def test_01(self) -> None:
        """测试滚动条显示策略"""
        # 水平滚动条效果与垂直滚动条相仿，这里仅演示垂直滚动条

        # 设置滚动条显示策略
        # self.pte.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # 默认值，仅在需要时显示滚动条
        # self.pte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 任何情况都不显示滚动条
        self.pte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 始终显示滚动条

        print(self.pte.verticalScrollBarPolicy())  # 获取垂直滚动条策略


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
