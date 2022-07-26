import sys

from PySide6 import QtCore, QtWidgets

"""
QDial 功能
旋钮控件提供了刻度、是否环绕等功能

.setWrapping(on: bool)             设置是否开启环绕，即不在下方留有缺口，而最大值最小值位置紧贴
.wrapping() -> bool                获取是否开启了环绕
.setNotchesVisible(visible: bool)  设置刻度是否可见
.notchesVisible() -> bool          获取刻度是否可见
.setNotchTarget(target: float)     设置刻度间的间距，单位为像素，默认值3.7
.notchTarget() -> float            获取刻度间距
.notchSize() -> int                获取当前刻度尺寸

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("空白测试模板")
        self.resize(800, 600)
        self.setup_ui()
        self.test()

    def setup_ui(self) -> None:
        """设置界面"""

        self.dial = QtWidgets.QDial(self)
        self.dial.move(200, 200)

        info_label = QtWidgets.QLabel(self)
        info_label.move(320, 230)

        @QtCore.Slot(int)
        def show_value(value: int):
            info_label.setText(f"旋钮的值变成了{value}")
            info_label.adjustSize()

        self.dial.valueChanged.connect(show_value)  # type: ignore

    def test(self) -> None:
        """测试QDial功能"""

        # 开启环绕
        self.dial.setWrapping(True)

        # 使刻度可见，并调整尺寸
        self.dial.setNotchesVisible(True)
        self.dial.setNotchTarget(10.8)
        print(self.dial.notchSize())  # 获取当前刻度线尺寸


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
