"""
对话框-模态与非模态

模态对话框的特点是会阻塞用户对同一应用程序的其他窗口的交互。即，用户必须先与对话框完成交互（点击「确定」按钮、
完成文件选择、输入了信息……）之后才能继续操作主窗口。
模态对话框又分为「应用程序级模态对话框」与「窗口级」对话框，前者将阻塞与整个程序中任何窗口的交互（默认值），而后者
只阻塞与该对话框关联的窗口的交互。

对对话框窗口调用 exec() 方法即可以模态显示该对话框窗口，在用户与对话框交互结束后exec()将返回值
也可以设置.setModal(True)或QWidget.setWindowModality()，然后调用show()方法显示模态对话框，这会立即将控制权返回给调用者

非模态对话框则不会阻塞用户与应用程序其他窗口交互。
先将对话框显式设置为非模态，然后调用show()将显示非模态对话框。

可以通过QWidget.setWindowModality方法显式指定对话框窗口的模态状态
QWidget.setWindowModality(window_modality: Qt.setWindowModality)   显式指定窗口模态，默认值为Qt.NonModal

Qt.WindowModality枚举值具体有如下几种：
https://doc.qt.io/qt-6/qt.html#WindowModality-enum
Qt.NonModal          窗口为非模态，不阻塞其他窗口的输入
Qt.WindowModal       窗口对单个窗口结构层次为模态，阻塞对其父窗口（及其的兄弟窗口）、祖父窗口（及其兄弟窗口）的输入
Qt.ApplicationModal  窗口对应用程序为模态，阻塞对所有窗口的输入
"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("模态与非模态对话框")
        self.resize(400, 400)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        line_edit = QtWidgets.QLineEdit(self)
        line_edit.setPlaceholderText("用于测试交互状态的LineEdit")

        # 设置对话框窗口
        dialog_window = QtWidgets.QMessageBox(self)  # 使用QDialog的子类来测试
        dialog_window.setWindowTitle("模态/非模态对话框")
        dialog_window.setText("模态窗口将阻塞用户对其他窗口的输入")
        dialog_window.setIcon(QtWidgets.QMessageBox.Icon.Information)

        # ================测试模态窗口=================================
        test_button_1 = QtWidgets.QPushButton("打开模态窗口")
        # 应用程序级模态
        # test_button_1.clicked.connect(dialog_window.exec)  # type: ignore
        # 窗口级模态
        test_button_1.clicked.connect(dialog_window.open)  # type: ignore

        # ================测试非模态窗口=================================
        def show_non_modal():
            dialog_window.setModal(False)
            dialog_window.show()

        test_button_2 = QtWidgets.QPushButton("打开非模态窗口")
        test_button_2.clicked.connect(show_non_modal)  # type: ignore

        # 使用布局管理器布局控件
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(test_button_1)
        layout.addWidget(test_button_2)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
