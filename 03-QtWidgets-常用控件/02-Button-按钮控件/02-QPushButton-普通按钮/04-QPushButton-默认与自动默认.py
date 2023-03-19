"""
QPushButton 默认按钮与自动默认

建议参考：https://doc.qt.io/qt-6/qpushbutton.html#default-prop
因为涉及对话框相关内容，首次学习时可略过此节，待学习对话框章节之后再回顾本节

===================================default属性=============================
默认和自动默认按钮决定当用户在对话框中按下 Enter 时会发生什么。

default 属性设置为 true 的按钮（即对话框的默认按钮）将在用户按下 Enter 时自动被按下，
但有一个例外：如果 autoDefault 按钮当前具有焦点，则按下 autoDefault 按钮。
当对话框有 autoDefault 按钮但没有默认按钮时，按 Enter 将按下当前具有焦点的 autoDefault 按钮，或者如果没有按钮具有焦点，
则按下焦点链中的下一个 autoDefault 按钮。

在对话框中，一次只能有一个按钮作为默认按钮。此按钮会显示一个额外边框（取决于 GUI 样式）。

默认按钮行为仅在对话框中提供。当按钮具有焦点时，始终可以通过按空格键从键盘单击按钮。

当对话框可见时，将当前默认按钮的默认属性设置为 False,则在对话框中的按钮下次获得焦点时，将自动分配一个新的默认

该属性的默认值为 False

===================================auto-default属性=============================
此属性用于保持按钮是否为自动默认按钮

如果这个属性被设置为 True，那么这个按钮就是一个自动默认按钮。

在一些 GUI 风格中，默认按钮的周围会有一个额外的框架，最多可达3个像素或更多。Qt会自动在自动默认按钮周围保留这个空间，也就是说，自动默认按钮可能有一个稍大的尺寸提示。

对于有 QDialog 父级的按钮，这个属性的默认值是真，否则默认为假。

关于 default 和 auto-default 如何交互的细节，请参见 default 属性。

===================================代码=============================
.isDefault() -> bool     设置为默认/非默认
.setDefault(bool)        获取默认状态
.setAutoDefault(bool)    设置为自动默认/非自动默认
.autoDefault() -> bool   获取自动默认状态
"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPushButton-默认按钮")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        # 创建信息提示框（一种可以包含按钮的对话框）并配置
        message_box = QtWidgets.QMessageBox(self)
        message_box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        message_box.setWindowTitle("这是一个消息提示框")
        message_box.setText("测试默认按钮功能")
        self.cancel_btn = message_box.addButton(
            QtWidgets.QMessageBox.StandardButton.Cancel
        )  # 添加标准按钮，返回值为按钮实例
        self.ok_btn = message_box.addButton(
            QtWidgets.QMessageBox.StandardButton.Ok
        )  # 添加标准按钮，返回值为按钮实例
        # 如果有按钮被按下，则将该按钮的文本打印到终端。
        message_box.buttonClicked.connect(lambda btn: print(btn.text()))  # type: ignore

        # 在主界面上添加一个弹出对话框的按钮，本节功能演示在对话框窗口中而非主窗口中呈现
        pop_btn = QtWidgets.QPushButton("弹出对话框", self)
        pop_btn.move(200, 200)
        pop_btn.clicked.connect(message_box.open)  # type: ignore

        self.test()

    def test(self):
        """测试按钮默认与自动默认功能"""
        self.ok_btn.setDefault(True)
        self.ok_btn.setAutoDefault(True)
        print(f"ok_btn.isDefault({self.ok_btn.isDefault()})")
        print(f"cancel_btn.isDefault({self.cancel_btn.isDefault()})")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
