import sys

from PySide6 import QtWidgets

"""
QFileDialog 功能作用

============================== 接受模式 ========================
通过接受模式来决定对话框用于打开文件还是保存文件

.setAcceptMode(mode: QFileDialog.AcceptMode)   设置接受模式
.acceptMode() -> QFileDialog.AcceptMode        获取当前的接受模式

AcceptMode具体有打开和保存两种：
QFileDialog.AcceptOpen                         打开文件，默认值
QFileDialog.AcceptSave                         保存文件

=============================== 选项 ==========================
可以通过对options属性的设置来调整对话框的外观（详见附录QFileDialog.Options枚举值）
默认情况下禁用所有选项
尽可能在更改对话框属性或显示对话框前设置这些选项，因为对话框已经可见时再设置选项可能不会立即生效

.setOptions(options: QFileDialog.Options)      设置选项，多个选项间使用|连接
.setOption(option: QFileDialog.Option, on: bool = True)  设置选项，通过on表示该选项的开关
.options() -> QFileDialog.Options              获取已设置的选项

QFileDialog.Options枚举值详见附录

============================== 视图模式 ========================
可以通过改变视图模式属性来控制对话框中显示的详细程度

.setViewMode(mode: QFileDialog.ViewMode)       设置视图模式（默认为Detail）
viewMode() -> QFileDialog.ViewMode             获取视图模式

视图模式枚举值有两种：
QFileDialog.Detail
QFileDialog.List

============================= 文件模式 ========================
设置文件模式属性，以定义用户希望在对话框中选择的项目的数量和类型

.setFileMode(mode: QFileDialog.FileMode)      设置文件模式，默认为AnyFile
.fileMode() -> QFileDialog.FileMode           获取文件模式

QFileDialog.FileMode枚举值详见附录

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QFileDialog-功能测试")
        self.dialog = QtWidgets.QFileDialog(self)
        self.setup_dialog()  # 在展示对话框前先完成设置
        self.setup_ui()

    def setup_dialog(self) -> None:
        """设置文件对话框"""

        # 接受模式
        self.dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)  # 文件将用于打开

        # 设置选项
        self.dialog.setOptions(
            QtWidgets.QFileDialog.Option.DontUseCustomDirectoryIcons  # 只使用默认目录图标（提高性能）
            | QtWidgets.QFileDialog.Option.DontConfirmOverwrite  # 当用户选中现有文件时则无需确认
        )

        # 设置视图模式
        # self.dialog.setViewMode(QtWidgets.QFileDialog.Detail)  # 显示详细信息（默认）
        self.dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.List)  # 显示列表信息

        # 文件模式
        self.dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)  # 只能选择单个现有文件

    def setup_ui(self) -> None:
        """设置界面"""

        self.resize(800, 600)
        browse_btn = QtWidgets.QPushButton("选择单个文件", self)
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
