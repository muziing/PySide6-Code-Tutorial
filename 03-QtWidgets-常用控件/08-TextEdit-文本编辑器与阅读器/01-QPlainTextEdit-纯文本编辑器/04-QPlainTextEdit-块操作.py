import sys

from PySide6 import QtCore, QtWidgets

"""
QPlainTextEdit 块操作
QPlainTextEdit将文本内容的每个段落视为一个「块」(block)，
段落（块）是一个格式化的字符串，为了适应控件的宽度，会自动换行。
默认情况下，在读取纯文本时，一个换行符表示一个段落。
文档由零个或多个段落组成。段落由硬线断开分隔。
段落中的每个字符都有自己的属性，例如字体和颜色。

.blockCount() -> int  获取文档中文本块的数量。默认情况下，对空的文档，块数为1

可以限制块的最大数量。当文档中块的数量超过此处设定的值时，文档最开始的块将被删除。
若文档包含的块的数量没有限制，则属性值为负数或0。默认值为0。
注意设置此功能后会禁用撤销/重做历史。

.setMaximumBlockCount(maximum: int)   设置最大块数量
.maximumBlockCount() -> int           返回最大块数量
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
        self.pte.resize(400, 400)
        self.pte.move(100, 100)
        self.button = QtWidgets.QPushButton("获取块数量", self)
        self.button.move(550, 200)

    def test_01(self) -> None:
        """测试块操作"""
        # 限制最大块数量
        self.pte.setMaximumBlockCount(5)
        print(self.pte.maximumBlockCount())

        # 获取块数量
        @QtCore.Slot()
        def test_slot():
            print(self.pte.blockCount())

        self.button.clicked.connect(test_slot)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
