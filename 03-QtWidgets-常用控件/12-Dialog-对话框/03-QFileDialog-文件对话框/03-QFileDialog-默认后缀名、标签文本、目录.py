import sys

from PySide6 import QtWidgets

"""
QFileDialog

============================ 默认后缀名 ============================
如果用户保存文件时没有指定其他后缀名，则使用默认后缀名
如果首字符为点（.）则将被移除

.setDefaultSuffix(suffix: str)
.defaultSuffix() -> str
============================ 标签文本 ============================
可以对标签文本设定自定义的文本，详情见附录中QFileDialog.DialogLabel枚举值

.setLabelText(label: QFileDialog.DialogLabel, text: str)
.labelText(label: QFileDialog.DialogLabel) -> str

============================== 目录 ============================
可以指定文件对话框当前显示的目录，或获取当前显示的目录

.setDirectory(directory: str)
.setDirectory(directory: QDir)
.setDirectoryUrl(directory: Qurl)
.directory() -> QtCore.QDir
.directoryUrl() -> QUrl
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialog = QtWidgets.QFileDialog(self)
        self.setup_dialog()  # 在展示对话框前先完成配置
        self.setup_ui()

    def setup_dialog(self) -> None:
        """设置文件对话框"""

        self.dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)  # 文件对话框用于保存文件

        # 默认后缀名
        self.dialog.setDefaultSuffix("txt")  # 设置默认后缀名

        # 标签文本
        self.dialog.setLabelText(QtWidgets.QFileDialog.DialogLabel.Accept, "保存")  # 将Accept按钮文本设置为保存
        self.dialog.setLabelText(QtWidgets.QFileDialog.DialogLabel.Reject, "取消")  # 将Reject标签文本设置为取消

    def setup_ui(self) -> None:
        """设置界面"""

        self.setWindowTitle("QFileDialog-功能测试")

        # 创建其他控件
        info_le = QtWidgets.QLineEdit(self)
        info_le.setMinimumWidth(600)
        browse_btn = QtWidgets.QPushButton("保存文件", self)
        info_label = QtWidgets.QLabel(self)

        # 连接信号与槽
        browse_btn.clicked.connect(self.dialog.open)  # type: ignore
        self.dialog.fileSelected.connect(lambda path: info_le.setText(path))  # type: ignore

        def show_current_dir():
            """在info_label中展示当前所在的目录"""
            dir_ = self.dialog.directory().path()  # 通过.path()获取str型的路径
            info_label.setText(dir_)

        self.dialog.currentChanged.connect(show_current_dir)  # type: ignore

        # 使用布局管理器布局
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(info_le)
        layout.addWidget(browse_btn)
        layout.addWidget(info_label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
