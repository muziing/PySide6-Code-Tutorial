"""
QMessageBox 静态方法

在某些场景下，只需显示一些简单的信息，并不需要实例化一个QMessageBox对象并对其各种属性进行复杂精细的设置，
而只需调用QMessageBox提供的静态方法即可满足这些需求

此处简单列出这些静态方法与其作用，参数返回值详解见下方讲解：
 - about()          显示关于信息
 - aboutQt()        显示当前程序使用的Qt的关于信息
 - information()    显示信息
 - question()       显示问题
 - warning()        显示警告
 - critical()       显示严重错误


.about(parent: QWidget, title: str, text: str) -> None
about方法用于显示一个简单的「关于」对话框，title、text、parent对应其窗口标题、正文文本、父控件，该窗口还有一个OK按钮
about会尝试寻找合适的图标应用于自身，具体规则参考https://doc.qt.io/qt-6/qmessagebox.html#about

.aboutQt(parent: QWidget, title:str = QString()) -> None
显示一个关于Qt的简易信息框，使用给定的窗口标题，并在位置上以父控件为中心。此消息中包含应用程序正在使用的Qt版本号
常用于应用程序的帮助菜单；QApplication 以槽的形式提供此功能

.information(parent: QWidget, title: str, text: str, button0: QMessageBox.StandardButton, \
button1: QMessageBox.StandardButton = QMessageBox.StandardButton.NoButton) -> QMessageBox.StandardButton
.information(parent: QWidget, title: str, text: str, buttons: QMessageBox.StandardButtons = \
QMessageBox.StandardButton.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.StandardButton.NoButton) -> \
QMessageBox.StandardButton

在指定的父窗口前打开一个具有指定标题和文本的信息提示框；
添加指定的标准按钮有两种方式（重载），若传入一组按钮（通过"|"连接），则必须将其中之一指定为defaultButton；
此静态方法会返回用户点击的标准按钮的id，如果用户通过Esc关闭对话框，则返回escape按钮；
此信息框为应用程序级模态对话框。

question()、warning()、critical() 静态方法与 information() 非常相似，类比使用即可，不再赘述。

"""

import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMessageBox, QPushButton, QWidget


class MyWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.about_btn = QPushButton("关于此程序")
        self.about_qt_btn = QPushButton("关于Qt")
        self.information_btn = QPushButton("展示信息")
        self.warning_btn = QPushButton("展示警告")
        self.label = QLabel()
        self.setup_ui()
        self.test_static()

    def setup_ui(self) -> None:
        """设置界面"""
        self.setWindowTitle("QMessageBox-静态方法")
        self.setMinimumSize(600, 180)

        layout = QHBoxLayout()
        layout.addWidget(self.about_btn)
        layout.addWidget(self.about_qt_btn)
        layout.addWidget(self.information_btn)
        layout.addWidget(self.warning_btn)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def test_static(self):
        """测试QMessageBox的静态方法"""

        self.about_btn.clicked.connect(
            lambda: QMessageBox.about(self, "关于此程序", "本程序为PySide6 Code Tutorial中的一个案例")
        )  # type: ignore
        self.about_qt_btn.clicked.connect(lambda: QMessageBox.aboutQt(self))  # type: ignore

        user_result_dict = {
            QMessageBox.StandardButton.Ok: "OK",
            QMessageBox.StandardButton.Cancel: "取消",
            QMessageBox.StandardButton.Discard: "不保存",
            QMessageBox.StandardButton.Save: "保存",
            QMessageBox.StandardButton.Apply: "应用",
        }

        @QtCore.Slot()
        def show_info_dlg() -> None:
            """self.information_btn对应的槽函数"""
            result = QMessageBox.information(
                self,
                "静态方法-信息",
                "这里可以展示一些信息",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Cancel,
            )  # 调用静态函数展示信息，将返回值保存到result变量中
            self.label.setText(f"用户选择了：{user_result_dict[result]}")
            self.label.adjustSize()

        @QtCore.Slot()
        def show_warn_dlg() -> None:
            """self.warning_btn对应的槽函数"""
            result = QMessageBox.warning(
                self, "静态方法-警告", "警告：直接退出将不会保存修改", QMessageBox.StandardButton.Discard
            )
            self.label.setText(f"用户选择了：{user_result_dict[result]}")
            self.label.adjustSize()

        self.information_btn.clicked.connect(show_info_dlg)  # type: ignore
        self.warning_btn.clicked.connect(show_warn_dlg)  # type: ignore


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
