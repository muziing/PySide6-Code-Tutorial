"""
QFormLayout  表单布局

表单布局专为「表单」使用场景设计优化，特点是有两列控件，左侧的为label标签，右侧的为field字段
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFormLayout.html
继承自QLayout

创建时可选传入父控件，（即使没有显式设置，也会在调用setLayout()方法时自动建立父子关系）
.__init__(self, parent: Optional[QWidget] = None)

"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QFormLayout")
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        name_le = QtWidgets.QLineEdit(self)
        age_label = QtWidgets.QLabel("年龄：", self)
        age_spinbox = QtWidgets.QSpinBox(self)
        age_spinbox.setRange(1, 150)
        age_spinbox.setValue(20)

        layout = QtWidgets.QFormLayout(self)
        layout.addRow("姓名：", name_le)
        layout.addRow(age_label, age_spinbox)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
