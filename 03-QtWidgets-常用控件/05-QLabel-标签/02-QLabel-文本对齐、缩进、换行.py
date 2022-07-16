import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

"""
QLabel 文本的对齐、缩进、换行

=================================== 对齐 ===================================

.setAlignment(Qt.Alignment)    设置文本对齐方式，详见下方Qt.Alignment
.alignment() -> Qt.Alignment   获取文本对齐方式

默认对齐方式为 Qt.AlignLeft | Qt.AlignVCenter，即水平靠左、垂直居中对齐


Qt.AlignmentFlag 中又分为水平对齐方式与垂直对齐方式，具体有如下数种：
https://doc.qt.io/qt-6/qt.html#AlignmentFlag-enum

水平对齐：
Qt.AlignLeft      与左边缘对齐
Qt.AlignRight     与右边缘对齐
Qt.AlignHCenter   在可用空间中水平居中
Qt.AlignJustify   两端对齐（尽可能使文字占满横向空间）

垂直对齐：
Qt.AlignTop       与顶部对齐
Qt.AlignBottom    与底部对齐
Qt.AlignVCenter   在可用空间中垂直居中
Qt.AlignBaseline  与基线对齐

若需同时设置水平、垂直两个维度的对齐方式，只需将两个Flags用或运算符连接，例如：
Qt.AlignCenter 等价于 Qt.AlignVCenter | Qt.AlignHCenter


=================================== 缩进 ===================================

.setIndent(indent: int)        设置缩进，默认为-1，即不进行缩进
.indent() -> int               获取缩进数

缩进的方向与对齐方向有关，Qt.AlignLeft则缩进出现在左边缘，Qt.AlignTop则出现在上边缘，以此类推

如果 indent 为负数，或者没有设置缩进，则label计算有效缩进的方法如下：
若 frameWidth() 为0，则有效缩进变为0；若 frameWidth() 大于0，则有效缩进为控件当前 font() 的
"x" 字母宽度的一半

=================================== 换行 ===================================
QLabel 可以开启自动换行功能，即在需要时从单词之间换行

.setWordWrap(on: bool)   设置是否开启自动换行，默认关闭
.wordWrap() -> bool      获取是否开启自动换行

"""

description = """QLabel is used for displaying text or an image. No user interaction functionality is provided.
The visual appearance of the label can be configured in various ways,
and it can be used for specifying a focus mnemonic key for another widget."""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLabel-文本操作")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面与测试功能"""
        label = QtWidgets.QLabel(self)
        # 手动设置尺寸，而非由内容自动设置
        label.resize(300, 300)
        label.move((self.width() - label.width()) // 2, (self.height() - label.height()) // 2)
        label.setStyleSheet("background-color: cyan;")

        # 注意测试以下三种功能时，会相互影响。
        # 如改变对齐方式会改变缩进方向、开启自动换行时每一行都会受到缩进影响等。

        # ==========测试对齐方式============
        label.setText("PySide6 Code Tutorial")  # 建议测试对齐方式功能时使用这个短内容文本
        # label.setAlignment(Qt.AlignTop)  # 上对齐
        # label.setAlignment(Qt.AlignJustify)  # 两侧对齐

        # label.setAlignment(Qt.AlignCenter)  # 居中对齐，等价于下一行
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 居中对齐

        # =========测试缩进=================
        # label.setText(description)
        # label.setIndent(30)  # 设置缩进，缩进方向对对齐方向相关
        print(label.indent())

        # =========测试自动换行=============
        # label.setText(description)
        label.setWordWrap(True)  # 若关闭自动换行，则超出单行的部分无法显示
        print(label.wordWrap())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
