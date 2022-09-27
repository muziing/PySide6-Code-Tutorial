import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QDir

"""
QFileDialog 过滤器

================================ 目录过滤器 ===================================
文件对话框支持QDir.Filters式过滤器，可以只显示满足过滤器要求的文件/目录

QDir.Filters枚举值详情参见本节附录

.setFilter(filters: QDir.Filters)
.filter() -> QDir.Filters

================================ 名称过滤器 ===================================
支持按文件名称设置过滤器，主要用*通配符与扩展名来限制文件类型

.setNameFilters(filters: Sequence[str])
.setNameFilter(filter: str)
.nameFilters() -> List[str]

============================== 媒体类型过滤器 =================================
还支持按媒体类型（MIME类型）分类过滤
这是setNameFilters()的便捷方法
调用setMimeTypeFilters会覆盖任何先前设置的名称过滤器，并更改nameFilters()的返回值

关于什么是MIME，可以参考：https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types

.setMimeTypeFilters(filters: Sequence[str])
.mimeTypeFilters() -> List[str]
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialog = QtWidgets.QFileDialog(self)
        self.setup_dialog()  # 在展示对话框前先完成设置
        self.setup_ui()

    def setup_dialog(self) -> None:
        """设置文件对话框"""

        # QDir过滤器
        self.dialog.setFilter(QDir.NoDotAndDotDot)  # 不显示.和..，主要在类Unix系统下有意义

        # 名称过滤器（会被设置MIME覆盖掉，测试时需注释掉MIME过滤器部分）
        self.dialog.setNameFilters(
            ("Python files (*.py *.pyi *.pyc *.pyw)", "Markdown files (*.md)", "Any files (*)")
        )

        # MIME过滤器
        # self.dialog.setMimeTypeFilters(("text/markdown", "image/jpeg", "application/octet-stream"))
        print(self.dialog.nameFilters())

    def setup_ui(self) -> None:
        """设置界面"""

        self.setWindowTitle("QFileDialog-过滤器")
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
