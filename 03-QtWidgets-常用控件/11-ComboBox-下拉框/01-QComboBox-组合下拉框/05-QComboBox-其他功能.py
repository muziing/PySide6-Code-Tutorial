import sys

from PySide6 import QtCore, QtWidgets

"""
QComboBox

设置是否具有边框，默认值为True
.setFrame(enable: bool)
.hasFrame() -> bool

当设置了无效索引时将显示占位文本
.setPlaceholderText(placeholder_text: str)
.placeholderText() -> str

清空条目与清空单行编辑器功能
.clear()
.clearEditText()

可以通过调用方法来编程弹出/收回下拉框
.showPopup()
.hidePopup()

设置补全器与验证器（详细内容见本项目QCompleter、QValidator章节）
.setCompleter(completer: QCompleter)
.setValidator(validator: QValidator)
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("空白测试模板")
        self.resize(800, 600)
        self.setup_ui()
        self.test()

    def setup_ui(self) -> None:
        """设置界面"""
        self.cbb = QtWidgets.QComboBox(self)
        self.cbb.move(200, 200)
        self.cbb.addItems([str(i) for i in range(100, 105)])  # 通过列表推导式快速添加多个条目

        self.button = QtWidgets.QPushButton("测试按钮", self)
        self.button.move(400, 200)

    def test(self) -> None:
        """测试combobox功能"""

        # 允许编辑
        self.cbb.setEditable(True)

        # 设置边框
        self.cbb.setFrame(False)

        @QtCore.Slot()
        def test_popup():
            """测试弹出下拉框功能"""
            self.cbb.showPopup()
            # self.cbb.hidePopup()

        self.button.clicked.connect(test_popup)  # type: ignore

        # 测试补全器
        self.cbb.setCompleter(QtWidgets.QCompleter(["abc", "106", "1001"]))

        # 测试清空
        self.cbb.clearEditText()  # 清除单行编辑器中的文本
        # self.cbb.clear()  # 清除所有条目


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
