"""
QMessageBox 按钮

对于每个按钮，需要为其定义「按钮角色」，如“接受”、“拒绝”、“应用”等（详见附录枚举值列表），用于描述按钮行为，
便于QMessageBox对不同角色的按钮进行处理，而与按钮上显示的文字无关。

同时消息提示框也提供了大量可选的标准按钮（详见枚举值列表），覆盖了绝大多数使用场景，一般直接添加标准按钮即可

一般直接设置标准按钮即可，将多个标准按钮用"|"连接传入即可：
.setStandardButtons(buttons: QMessageBox.StandardButtons)           设置标准按钮
.standardButtons() -> QMessageBox.StandardButtons                   获取当前设置的标准按钮

添加按钮函数有3种重载，返回值也有所不同，调用时需要注意参数：
.addButton(button: QAbstractButton, role: QMessageBox.ButtonRole) -> None  将按钮button添加到信息提示框并赋予指定的角色
.addButton(text: str, role: QMessageBox.ButtonRole) -> QPushButton         使用给定的text创建按钮，并按给定的角色添加
.addButton(button: QMessageBox.StandardButton) -> QPushButton              向信息提示框中添加标准按钮，并返回该按钮

还可以指定默认按钮（用户在对话框交互时直接按下Enter激活的按钮）、Esc按钮（用户按下键盘Esc键时触发的按钮）
.setDefaultButton(button: QPushButton) -> None                     将button设置为信息提示框的默认按钮
.setEscapeButton(button: QAbstractButton) -> None                  若用户通过键盘Esc键与对话框交互，则激活button按钮

获取按钮、按钮角色：
.button(which: QMessageBox.StandardButton) -> QAbstractButton      通过标准按钮返回该按钮的实例
.buttons() -> List[QAbstractButton]                                返回已经添加的按钮的列表
.buttonRole(button: QAbstractButton) -> QMessageBox.ButtonRole     返回特定按钮的角色,若按钮为None或未被添加则返回InvalidRole

若需移除按钮，则调用removeButton并将按钮作为参数传入：
.removeButton(button: QAbstractButton) -> None                     从按钮框中移除button但不删除它

"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QMessageBox-按钮")
        self.resize(800, 600)
        self.message_box = QtWidgets.QMessageBox(self)  # 创建对话框
        self.setup_message_box()
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 在主界面上弹出对话框
        pop_btn = QtWidgets.QPushButton("弹出对话框", self)
        pop_btn.move(200, 200)
        pop_btn.clicked.connect(self.message_box.open)  # type: ignore

    def setup_message_box(self) -> None:
        """设置对话框"""

        self.message_box.setWindowTitle("按钮功能测试")
        self.message_box.setText("一段对话框正文文本")

        # 设置标准按钮
        self.message_box.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel
        )

        # 设置默认按钮、Esc按钮
        self.message_box.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
        self.message_box.setEscapeButton(
            self.message_box.button(QtWidgets.QMessageBox.StandardButton.Cancel)
        )

        # 添加按钮
        self.message_box.addButton(
            "自定义按钮", QtWidgets.QMessageBox.ButtonRole.AcceptRole
        )  # 通过自定义文本与按钮角色添加
        discard_btn = self.message_box.addButton(
            QtWidgets.QMessageBox.StandardButton.Discard
        )  # 添加标准按钮，返回值为按钮实例

        # 获取按钮角色
        print(self.message_box.buttonRole(discard_btn))  # 将discard_btn按钮的角色打印到终端

        # 移除按钮
        self.message_box.removeButton(discard_btn)  # 将按钮实例作为参数传入即可移除

        # 如果有按钮被按下，则将该按钮的文本打印到终端。此信号会在“QMessageBox-信号”小节中讲解。
        self.message_box.buttonClicked.connect(lambda btn: print(btn.text()))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
