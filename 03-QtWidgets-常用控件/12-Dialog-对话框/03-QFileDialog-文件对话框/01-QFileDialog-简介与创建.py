import sys

from PySide6 import QtWidgets

"""
QFileDialog 文件对话框

用户可以通过文件对话框浏览文件或目录，常用于选择打开文件、将当前文件保存到某处等场景
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFileDialog.html
继承自 QDialog

有两种构造函数，简洁版只可选地传入父控件与窗口标志，完整版可以在创建时定义更多属性功能：
.__init__(self, parent: QWidget, f: QtCore.Qt.WindowFlags)
.__init__(self, parent: Optional[QWidget] = None, caption: str = '', directory: str = '', filter: str = '')

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QFileDialog-简介")
        self.dialog = QtWidgets.QFileDialog(self)
        self.setup_dialog()
        self.setup_ui()

    def setup_dialog(self) -> None:
        """配置对话框属性功能"""
        self.dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)  # 打开模式
        self.dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)  # 选择现有文件
        self.dialog.setLabelText(QtWidgets.QFileDialog.DialogLabel.Accept, "选择")  # 为「接受」按键指定文本
        self.dialog.setLabelText(QtWidgets.QFileDialog.DialogLabel.Reject, "取消")  # 为「拒绝」按键指定文本

    def setup_ui(self) -> None:
        """设置界面"""
        self.resize(800, 600)
        browse_btn = QtWidgets.QPushButton("选择文件", self)
        browse_btn.move(150, 200)
        browse_btn.clicked.connect(self.dialog.open)  # type: ignore
        info_le = QtWidgets.QLineEdit(self)
        info_le.move(150, 250)
        info_le.setMinimumWidth(600)
        self.dialog.fileSelected.connect(lambda path: info_le.setText(path))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
