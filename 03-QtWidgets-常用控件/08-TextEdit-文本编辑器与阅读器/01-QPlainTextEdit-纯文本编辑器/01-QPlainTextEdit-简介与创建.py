import sys

from PySide6 import QtWidgets

"""
QPlainTextEdit 纯文本编辑器
仅用于编辑纯文本的编辑器，性能比支持富文本的QTextEdit更佳
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPlainTextEdit.html
继承自QAbstractScrollArea

与QTextEdit功能相似，但针对纯文本处理进行了优化，差异：
QPlainTextEdit是一个简略版的类，使用QTextEdit和QTextDocument作为背后实现的技术支撑
性能优于QTextEdit，主要是因为在文本文档中使用QPlainTextDocumentLayout简化文本布局
纯文本文档布局不支持表格或嵌入框架，并使用逐行滚动的方式替换像素精确高度计算

两种构造函数，可以指定编辑器中的文本和父控件
__init__(self, parent: Optional[QWidget] = None)
__init__(self, text: str, parent: Optional[QWidget] = None)

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPlainTextEdit-创建")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面与测试创建QPlainTextEdit"""

        # pte = QtWidgets.QPlainTextEdit(self)  # 创建
        pte = QtWidgets.QPlainTextEdit(
            "https://github.com/muziing/PySide6-Code-Tutorial", self
        )  # 创建时附带文本内容

        pte.resize(300, 400)
        pte.move(100, 100)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
