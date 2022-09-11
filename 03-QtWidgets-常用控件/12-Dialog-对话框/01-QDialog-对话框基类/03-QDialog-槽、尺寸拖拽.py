import sys

from PySide6 import QtCore, QtWidgets

"""
QDialog 槽、结果、尺寸拖拽控件


QDialog有一组槽，用于显示、关闭对话框并返回结果：
.accept()             隐藏模态对话框，并将结果码设置为 QDialog.Accepted
.reject()             隐藏模态对话框，并将结果码设置为 QDialog.Rejected，键盘Esc键、直接关闭对话框也会触发
.open()               将对话框作为窗口级模态显示，立即返回
.done(r: int)         关闭对话框并将其结果码设置为r，finished()信号立即发射r。若此对话框以exec()显示，
                      则done()也将导致局部事件循环结束，且exec()返回r。
.exec()               将对话框作为模态对话框显示。（默认为应用程序级模态）此函数返回QDialog.Accepted或QDialog.Rejected。
                      尽量避免使用exec()函数，而用open()替代。因为open()是异步的，并且不会增加额外的事件循环
                 
QDialog.result中保存了对话框获得的结果，也可以通过代码显式设置结果码：
.result() -> int      获取模态对话框的结果码，QDialog.Accepted为1,QDialog.Rejected为0
.setResult(i: int)    将模态对话框的结果码设置为i

获取对话框结果码的几种方式：
  - .exec() 的返回值，例如 result = my_dialog.exec()
  - finished(result: int) 信号传递
  - .result() 的返回值

QDialog可以指定是否在窗口右下角显示一个QSizeGrip控件，方便用户将光标置于其上拖拽调整窗口大小
.setSizeGripEnabled(enable: bool)     设置是否使用尺寸拖拽控件（默认为否）
.isSizeGripEnabled() -> bool          获取尺寸拖拽控件启用状态

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QDialog-槽")
        self.resize(800, 600)
        self.dialog = QtWidgets.QDialog(self)
        self.setup_ui()
        self.setup_dialog()

    def setup_ui(self) -> None:
        """设置界面"""

        # 用于显示对话框
        open_dialog_btn = QtWidgets.QPushButton("打开对话框（Open）", self)
        open_dialog_btn.move(200, 200)
        open_dialog_btn.clicked.connect(self.dialog.open)  # type: ignore
        exec_dialog_btn = QtWidgets.QPushButton("打开对话框（Exec）", self)
        exec_dialog_btn.move(400, 200)
        exec_dialog_btn.clicked.connect(self.dialog.exec)  # type: ignore

        # 用于显示对话框返回值
        info_label = QtWidgets.QLabel(self)
        info_label.move(220, 300)

        @QtCore.Slot(int)
        def show_result(result: int) -> None:
            info_label.setText(f"对话框窗口的返回值为：{result}")
            info_label.adjustSize()

        self.dialog.finished.connect(show_result)  # type: ignore

    def setup_dialog(self) -> None:
        """设置对话框窗口"""
        self.dialog.setWindowTitle("对话框-测试槽功能")

        self.dialog.setSizeGripEnabled(True)  # 在对话框右下角显示易于拖拽控制窗口尺寸的把手

        btn_1 = QtWidgets.QPushButton("Accept")
        btn_1.clicked.connect(self.dialog.accept)  # type: ignore

        btn_2 = QtWidgets.QPushButton("Reject")
        btn_2.clicked.connect(self.dialog.reject)  # type: ignore

        btn_3 = QtWidgets.QPushButton("Done")
        spinbox = QtWidgets.QSpinBox()
        spinbox.setValue(50)

        # 将spinbox中用户设定的值作为对话框结果码返回
        btn_3.clicked.connect(lambda: self.dialog.done(spinbox.value()))  # type: ignore

        # 布局管理器
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(btn_1)
        layout.addWidget(btn_2)
        layout.addWidget(spinbox)
        layout.addWidget(btn_3)
        self.dialog.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
