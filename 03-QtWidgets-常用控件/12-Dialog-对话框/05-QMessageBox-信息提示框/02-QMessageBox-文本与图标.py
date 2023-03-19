"""
QMessageBox 文本与图标

=========================================文本==========================================
信息提示框中可以设置文本，根据重要程度、详细程度不同，
可以使用不同的API分别设置普通文本、详情文本、信息文本，在界面显示中样式会有所区别（取决于平台）

普通文本，信息框提示中的主要文本内容：
.setText(text:str)
.text() -> str

详情文本，会被显示在详情区域，用户需要点击“显示细节”按钮才会展示
注意text会被解析为纯文本
.setDetailedText(text: str)
.detailedText() -> str

信息文本，用于扩展text()以向用户提供更多信息。在MacOS上此文本会以小系统字体显示在text()下方
而对于其他平台，只会简单地附加到现有文本中
.setInformativeText(text: str)
.informativeText() -> str

=========================================图标==========================================
信息提示框可以在内部设置一个图标，该图标会出现在文本旁（而不同于一般的设置窗口图标）
设置图标有两种方式，其一为设置QMessageBox提供的标准图标，其二为自定义位图：

为消息提示框设置标准图标（警告图标、错误图标等），而非用户指定的QIcon对象，其样式由当前GUI样式风格决定

.setIcon(icon: QMessageBox.Icon)    为消息提示框设置图标，默认为QMessageBox.NoIcon
.icon() -> QMessageBox.Icon         获取当前设置的标准图标

QMessageBox.Icon枚举值详见本目录下对应附录小节

如要设置自定义图标，则应使用setIconPixmap方法：
.setIconPixmap(icon: QPixmap)       设置自定义图标，需要为位图形式
.iconPixmap() -> QPixmap            获取设置的图标
"""

import sys

from PySide6 import QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QMessage-文本与图标")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面与对话框"""

        message_box = QtWidgets.QMessageBox(self)
        message_box.setWindowTitle("MessageBox的窗口标题")

        # 设置文本
        message_box.setText("信息提示框中的一般文本")
        message_box.setDetailedText("这是一段详情文本")
        message_box.setInformativeText("这是一段信息文本")

        # 设置图标
        # message_box.setIcon(QtWidgets.QMessageBox.Icon.Information)  # 设置标准图标
        my_icon = QtGui.QPixmap("../../../Resources/Icons/Qt_for_Python_128px.png")
        message_box.setIconPixmap(my_icon)  # 设置自定义图标

        pop_btn = QtWidgets.QPushButton("弹出对话框", self)
        pop_btn.move(200, 200)
        pop_btn.clicked.connect(message_box.open)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
