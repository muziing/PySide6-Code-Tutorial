import sys

from PySide6 import QtCore, QtWidgets

"""
QAbstractSlider 数值范围、步长、值

可以通过如下方法，限制滑块的最大/小值、页步长（使用PageUp/PageDown键盘按键输入时每次按键变化的值）
、单步长（使用键盘方向键或鼠标滚轮每次移动的值）、设置滑块当前值与获取滑块当前值

.setMaximum(max: int)        设置最大值，默认为99
.maximum() -> int            获取当前设置的最大值
.setMinimum(mini: int)       设置最小值，默认为0
.minimum() -> int            获取当前设置的最小值

.setPageStep(step: int)      设置页步长，默认为10
.pageStep() -> int           获取当前设置的页步长
.setSingleStep(step: int)    设置单步长，默认值为1
.singleStep() -> int         获取当前设置的单步长

.setValue(value: int)        通过编程方式设置滑块当前值，若超出范围则取极限值
.value() -> int              获取滑块当前值
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractSlider-功能测试")
        self.resize(800, 600)
        self.setup_ui()
        self.test()

    def setup_ui(self) -> None:
        """设置界面"""

        self.slider = QtWidgets.QSlider(self)
        self.slider.move(200, 200)

        info_label = QtWidgets.QLabel(self)
        info_label.move(240, 200)

        @QtCore.Slot(int)
        def show_value(value: int):
            info_label.setText(f"滑块的值变成了{value}")
            info_label.adjustSize()

        self.slider.valueChanged.connect(show_value)  # type: ignore

    def test(self) -> None:
        """测试滑块数值范围、步长、值功能"""

        # 数值范围
        self.slider.setMaximum(200)
        self.slider.setMinimum(20)

        # 步长，通过键盘方向键、PageUp/PageDown、鼠标滚轮测试
        self.slider.setSingleStep(5)  # 设置单步长
        self.slider.setPageStep(20)  # 设置页步长

        # 设置滑块当前值
        self.slider.setValue(100)
        # self.slider.setValue(1000)  # 超过最大值限制，实际设置为最大值200
        print(self.slider.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
