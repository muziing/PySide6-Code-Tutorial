import sys
from pprint import pprint

from PySide6 import QtWidgets

"""
QFileDialog 信号

currentChanged(path: str)               当前选择改变时发射此信号，新选择的项作为参数传递
currentUrlChanged(url: QUrl)            当前选中的Url改变时发射此信号，新的Url作为参数传递
directoryEntered(directory: str)        进入目录时发射此信号，目录作为参数传递
directoryUrlEntered(directory: QUrl)    进入目录时发射此信号，目录的URL作为参数传递
fileSelected(file: str)                 选择了文件，并以Accept退出对话框时，发射此信号
filesSelected(selected: List[str])      选择了（多个）文件时发射此信号
filterSelected(filter_: str)             选中过滤器时发射此信号，过滤器作为参数传出
urlSelected(url: QUrl)                  选择了文件，并以Accept退出对话框时，发射此信号
urlsSelected(urls: List[QUrl])          选择了（多个）文件时发射此信号
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWidget, self).__init__(*args, **kwargs)

        self.dialog = QtWidgets.QFileDialog(self)  # 文件对话框
        self.info_le = QtWidgets.QLineEdit(self)  # 用于显示最终选择
        self.info_label = QtWidgets.QLabel(self)  # 用于显示当前选择

        self.setup_dialog()
        self.setup_ui()
        self.test_signals()

    def test_signals(self) -> None:
        """测试QFileDialog信号功能"""
        self.dialog.fileSelected.connect(lambda path: self.info_le.setText(path))  # type: ignore
        self.dialog.currentChanged.connect(lambda path: self.info_label.setText(path))  # type: ignore
        self.dialog.filesSelected.connect(lambda files: pprint(f"filesSelected: {files}"))  # type: ignore
        self.dialog.directoryEntered.connect(lambda dir_: print(f"directoryEntered: {dir_}"))  # type: ignore
        self.dialog.filterSelected.connect(lambda filter_: print(f"filterSelected: {filter_}"))  # type: ignore

    def setup_dialog(self) -> None:
        """设置文件对话框"""

        self.dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)
        self.dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        self.dialog.setNameFilters(
            ("Python files (*.py)", "Markdown files (*.md)", "Any files (*)")
        )

    def setup_ui(self) -> None:
        """设置界面"""

        self.setWindowTitle("QFileDialog-信号")

        # 配置其他控件
        self.info_le.setMinimumWidth(600)
        browse_btn = QtWidgets.QPushButton("打开文件", self)
        browse_btn.clicked.connect(self.dialog.open)  # type: ignore

        # 使用布局管理器布局
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(browse_btn)
        layout.addWidget(self.info_le)
        layout.addWidget(self.info_label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
