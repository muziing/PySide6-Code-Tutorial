import sys

from PySide6 import QtCore, QtWidgets

"""
QPlainTextEdit 编辑操作
QPlainTextEdit 提供了许多编辑文本相关的槽函数，可以使用这些槽函数完成特定功能

======================================= 槽函数 ==================================================

.clear()                     清空文本编辑器中的所有文字。注意所有撤销/重做记录也被清空
.setPlainText(text: str)     清空先前的文本，将编辑器中的文本设置为text。注意所有撤销/重做记录也被清空
.selectAll()                 选中所有文本
.copy()                      将选中的文本复制到剪切板中
.cut()                       将选中的文字复制到剪切板中，并将其从编辑器中删除
.paste()                     将剪切板中的文字粘贴至文本编辑器光标当前所在位置
.undo()                      撤销最后的操作
.redo()                      重做最后的操作
.insertPlainText(text: str)  在当前光标位置插入纯文本text，等价于.textCursor().insertText(text)
.appendPlainText(text: str)  将text作为一个新的段落，插入到文本编辑器末尾
.appendHtml(html: str)       将html作为一个新的段落插入到末尾
.centerCursor()              滚动文档，以使光标位于竖直居中位置

======================================= 其他 ==================================================
.setPlainText(text: str)           将text设置为编辑器中的文本，之前的文本、撤销/重做记录等全部清空
.toPlainText() -> str              将当前编辑器中的文本作为纯文本返回
.setUndoRedoEnable(enable: bool)   设置是否允许撤销/重做，默认允许
.isUndoRedoEnabled() -> bool       获取是否允许撤销/重做
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPlainTextEdit-编辑操作")
        self.resize(800, 600)
        self.setup_ui()
        self.pte_slot_test()
        self.test_edit()

    def setup_ui(self) -> None:
        """设置界面"""

        self.pte = QtWidgets.QPlainTextEdit()
        self.pte.resize(600, 450)

        # 槽函数相关
        self.clear_button = QtWidgets.QPushButton("清空")
        self.select_all_button = QtWidgets.QPushButton("全选")
        self.copy_button = QtWidgets.QPushButton("复制")
        self.cut_buton = QtWidgets.QPushButton("剪切")
        self.paste_button = QtWidgets.QPushButton("粘贴")
        self.undo_button = QtWidgets.QPushButton("撤销")
        self.redo_button = QtWidgets.QPushButton("重做")
        self.insert_line_edit = QtWidgets.QLineEdit()
        self.insert_line_edit.setPlaceholderText("插入纯文本")
        self.append_plain_line_edit = QtWidgets.QLineEdit()
        self.append_plain_line_edit.setPlaceholderText("追加纯文本")
        self.append_html_line_edit = QtWidgets.QLineEdit()
        self.append_html_line_edit.setPlaceholderText("追加HTML")
        self.center_cursor_button = QtWidgets.QPushButton("使光标居中")

        # 其他编辑功能
        self.output_text_button = QtWidgets.QPushButton("输出为纯文本")
        self.set_plain_text_button = QtWidgets.QPushButton("设置纯文本")
        self.undo_redo_enable_checkbox = QtWidgets.QCheckBox("允许撤销/重做")
        self.undo_redo_enable_checkbox.setChecked(True)

        # 将按钮通过布局管理器放在组框中，首次学习可忽略本段代码
        button_groupbox = QtWidgets.QGroupBox("编辑操作")
        layout = QtWidgets.QVBoxLayout(button_groupbox)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.select_all_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.cut_buton)
        layout.addWidget(self.paste_button)
        layout.addWidget(self.undo_redo_enable_checkbox)
        layout.addWidget(self.undo_button)
        layout.addWidget(self.redo_button)
        layout.addWidget(self.insert_line_edit)
        layout.addWidget(self.append_plain_line_edit)
        layout.addWidget(self.append_html_line_edit)
        layout.addWidget(self.center_cursor_button)
        layout.addWidget(self.output_text_button)
        layout.addWidget(self.set_plain_text_button)
        button_groupbox.setLayout(layout)

        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(self.pte)
        main_layout.addWidget(button_groupbox)
        self.setLayout(main_layout)

    def pte_slot_test(self) -> None:
        """测试QPlainTextEdit槽函数"""

        # 将各个按钮的点击信号与纯文本编辑器的槽函数连接
        self.clear_button.clicked.connect(self.pte.clear)  # type: ignore
        self.select_all_button.clicked.connect(self.pte.selectAll)  # type: ignore
        self.copy_button.clicked.connect(self.pte.copy)  # type: ignore
        self.cut_buton.clicked.connect(self.pte.cut)  # type: ignore
        self.paste_button.clicked.connect(self.pte.paste)  # type: ignore
        self.undo_button.clicked.connect(self.pte.undo)  # type: ignore
        self.redo_button.clicked.connect(self.pte.redo)  # type: ignore
        self.insert_line_edit.textChanged.connect(self.pte.insertPlainText)  # type: ignore
        self.append_plain_line_edit.textChanged.connect(self.pte.appendPlainText)  # type: ignore
        self.append_html_line_edit.textChanged.connect(self.pte.appendHtml)  # type: ignore
        self.center_cursor_button.clicked.connect(self.pte.centerCursor)  # type: ignore

    def test_edit(self) -> None:
        """测试其他编辑功能"""

        @QtCore.Slot()
        def to_plain_text_test():
            """测试以纯文本输出功能"""
            print(self.pte.toPlainText())

        @QtCore.Slot(str)
        def set_plain_text_test(text: str):
            """测试设置纯文本功能"""
            if text:
                self.pte.setPlainText(text)
            else:
                self.pte.setPlainText("https://github.com/muziing/PySide6-Code-Tutorial")

        @QtCore.Slot(bool)
        def undo_redo_enable_test(enable: bool):
            """测试禁用撤销/重做功能"""
            self.pte.setUndoRedoEnabled(enable)
            print(f"pte.isUndoRedoEnabled({self.pte.isUndoRedoEnabled()})")

        self.output_text_button.clicked.connect(to_plain_text_test)  # type: ignore
        self.set_plain_text_button.clicked.connect(set_plain_text_test)  # type: ignore
        self.undo_redo_enable_checkbox.toggled.connect(undo_redo_enable_test)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
