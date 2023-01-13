"""
QPlainText 案例：显示行号
每当文本文档需要更新显示矩形时，会发射updateRequest信号，垂直滚动量作为参数传出
利用这个信号，可以编写行号、断点等功能
"""

import sys

from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPlainTextEdit-显示行号")
        self.resize(800, 600)
        self.setup_ui()
        self.show_line_num()

    def setup_ui(self) -> None:
        """设置界面"""

        self.pte = QtWidgets.QPlainTextEdit(self)
        self.pte.resize(350, 400)
        self.pte.move(150, 80)
        self.pte.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)  # 始终显示滚动条

        # 用于限制line_num_label位置尺寸的父控件
        line_num_widget = QtWidgets.QWidget(self)
        line_num_widget.resize(30, 400)
        line_num_widget.move(120, 80)

        self.line_num_label = QtWidgets.QLabel(line_num_widget)
        self.line_num_label.move(0, 5)  # 微调，视觉上对齐
        line_nums = "\n".join([str(i) for i in range(1, 101)])  # 生成行号文本
        self.line_num_label.setText(line_nums)

    def show_line_num(self) -> None:
        """显示行号"""

        @QtCore.Slot(QtCore.QRect, int)
        def scroll_line_num(_, dy: int):  # 用_表示仅占位而不会用到的参数
            self.line_num_label.move(self.line_num_label.x(), self.line_num_label.y() + dy)

        self.pte.updateRequest.connect(scroll_line_num)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
