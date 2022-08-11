import sys

from PySide6 import QtGui, QtWidgets

"""
QLineEdit 验证器与掩码

单行文本编辑器可以设置验证器（Validator），比如限制只能输入一定范围内的数字等，设置验证器后，
只有满足验证器要求的字符才能被输入，否则用户输入不会显示在编辑器内
关于QValidator的详细信息，参考本项目QtGUI目录下对应小节

.setValidator(v: QValidator)         设置验证器
.validator() -> QValidator           获取验证器
可以通过调用.setValidator(0)来取消当前设置的验证器

掩码则是一种更为严格的验证方式，用户输入的每一个字符都必须严格符合该位掩码允许值
掩码可以单独使用，也可以与验证器配合使用
详情见文档：https://doc.qt.io/qt-6/qlineedit.html#inputMask-prop

.setInputMask(input_mask: str)       设置掩码
.inputMask() -> str                  获取当前掩码
可以通过调用.setInputMask("")来取消当前设置的掩码

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-验证器与掩码")
        self.resize(800, 600)
        self.setup_ui()
        self.test_validator()
        self.test_mask()

    def setup_ui(self) -> None:
        """设置界面"""

        self.line_edit = QtWidgets.QLineEdit()
        self.ip_line_edit = QtWidgets.QLineEdit()

        layout = QtWidgets.QFormLayout()
        layout.addRow(QtWidgets.QLabel("输入两位整数："), self.line_edit)
        layout.addRow(QtWidgets.QLabel("IPv4地址："), self.ip_line_edit)
        self.setLayout(layout)

    def test_validator(self) -> None:
        """测试验证器功能"""

        # 创建一个整数验证器对象，其特点为限制只能输入范围内的整数
        validator = QtGui.QIntValidator(10, 99, self.line_edit)
        # 将验证器设置给line_edit
        self.line_edit.setValidator(validator)

    def test_mask(self) -> None:
        """测试掩码功能"""

        # 创建掩码，详细语法见文档
        ip_address_mask = "000.000.000.000;_"  # 适用于IPv4地址的掩码，;后的_为占位符
        # 设置输入掩码
        self.ip_line_edit.setInputMask(ip_address_mask)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
