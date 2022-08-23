import sys

from PySide6 import QtWidgets

"""
QAbstractSpinBox 键盘追踪、加速、循环

=================================== 键盘追踪 ===================================
若启用了键盘追踪（默认值），则spinbox会在从键盘输入新值时发射 valueChanged() 和 textChanged() 信号
例如用户想要输入600，会在键盘上依次按下6、0、0，此时spinbox会发射三次信号，值分别为6、60和600
若禁用了键盘追踪，则spinbox在用户键盘输入时不会发射 valueChanged() 和 textChanged() 信号，
而是会在按下Enter、丢失键盘焦点或使用了按箭头键等其他spinbox功能时发射信号

.setKeyboardTracking(kt: bool)    设置是否启用键盘追踪
.keyboardTracking() -> bool       获取键盘追踪启用状态

=================================== 加速 ===================================
如果启用了加速功能，当长按上/下按钮以连续增加/减少数值设定框中的值时，速度会加快

.setAccelerated(on: bool)         设置加速功能是否启用
.isAccelerated() -> bool          获取加速功能启用状态

=================================== 循环 ===================================
如果启用了循环功能，则当值增加到最大值时继续增加，会跳转到最小值，反之亦然

.setWrapping(w: bool)             设置是否开启循环
.wrapping() -> bool               获取循环状态

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractSpinBox")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        spin_box = QtWidgets.QSpinBox(self)
        spin_box.move(200, 200)
        spin_box.setRange(0, 999)

        # 连接信号与槽，实时打印出valueChanged传出的值
        spin_box.valueChanged.connect(lambda val: print(f"spinbox的值变为了{val}"))  # type: ignore

        # 键盘追踪
        # 通过键盘键入多位数值，注意观察打印出的value
        # spin_box.setKeyboardTracking(True)
        spin_box.setKeyboardTracking(False)

        # 设置加速功能
        spin_box.setAccelerated(True)  # 启用加速功能，长按上下键值增减速度会加快

        # 设置循环功能
        spin_box.setWrapping(True)  # 从最小值继续减小会跳转到最大值，反之亦然


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
