import sys

from PySide6 import QtWidgets

"""
QDialog 信号

accepted()               用户接受对话框或调用accept()、done(QDialog.Accepted)时发射此信号
rejected()               用户拒绝对话框或调用reject()、done(QDialog.Rejected)时发射此信号
finished(result: int)    当通过用户操作、done()、accept()、reject()设置了对话框的结果码时发射此信号，结果码作为参数传递

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QDialog 信号")
        self.resize(800, 600)
        self.dialog = QtWidgets.QDialog(self)
        self.setup_dialog()
        self.setup_ui()

    def setup_dialog(self) -> None:
        """设置对话框窗口"""
        self.dialog.setWindowTitle("对话框-测试信号")

        accept_btn = QtWidgets.QPushButton("Accept")
        accept_btn.clicked.connect(self.dialog.accept)  # type: ignore

        reject_btn = QtWidgets.QPushButton("Reject")
        reject_btn.clicked.connect(self.dialog.reject)  # type: ignore

        done_btn = QtWidgets.QPushButton("Done")

        done_btn.clicked.connect(lambda: self.dialog.done(QtWidgets.QDialog.Accepted))  # type: ignore
        # done_btn.clicked.connect(lambda: self.dialog.done(QtWidgets.QDialog.Rejected))  # type: ignore

        # 布局管理器
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(accept_btn)
        layout.addWidget(reject_btn)
        layout.addWidget(done_btn)
        self.dialog.setLayout(layout)

    def setup_ui(self) -> None:
        """设置界面"""

        # 用于显示对话框
        open_dialog_btn = QtWidgets.QPushButton("打开对话框（Open）", self)
        open_dialog_btn.move(200, 200)
        open_dialog_btn.clicked.connect(self.dialog.open)  # type: ignore

        # 用于显示对话框返回值
        info_label_1 = QtWidgets.QLabel(self)
        info_label_1.move(220, 300)
        info_label_1.resize(200, 50)

        info_label_2 = QtWidgets.QLabel(self)
        info_label_2.move(220, 360)
        info_label_2.resize(200, 50)

        self.dialog.accepted.connect(lambda: info_label_1.setText("对话框窗口被接受了"))  # type: ignore
        self.dialog.rejected.connect(lambda: info_label_1.setText("对话框窗口被拒绝了"))  # type: ignore
        self.dialog.finished.connect(lambda result: info_label_2.setText(f"对话框窗口的返回值为：{result}"))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
