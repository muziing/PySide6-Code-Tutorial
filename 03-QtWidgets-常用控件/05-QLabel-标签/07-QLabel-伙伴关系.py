import sys

from PySide6 import QtWidgets

"""
QLabel 伙伴关系
当用户按下标签控件的快捷键（仅支持"字母&"形式）时，键盘焦点会转移到该标签的伙伴控件（比如文本编辑器）上

.setBuddy(buddy: QWidget)    设置标签的伙伴
.buddy() -> QWidget          获取标签的伙伴
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLabel-伙伴关系")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()

    def setup_ui(self) -> None:
        """设置界面"""
        self.name_label = QtWidgets.QLabel("&Name")  # Alt+N快捷键
        self.age_label = QtWidgets.QLabel("年龄(&A)")  # 使用Alt+A快捷键，age_spin_box即获得焦点
        self.name_edit = QtWidgets.QLineEdit()
        self.age_spin_box = QtWidgets.QSpinBox()

        # 使用表单布局管理器进行布局，更多信息参阅本项目Layout目录
        layout = QtWidgets.QFormLayout()
        layout.addRow(self.name_label, self.name_edit)
        layout.addRow(self.age_label, self.age_spin_box)
        self.setLayout(layout)

    def test_01(self) -> None:
        """测试伙伴关系功能"""
        self.name_label.setBuddy(self.name_edit)
        self.age_label.setBuddy(self.age_spin_box)

        print(self.name_label.buddy())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
