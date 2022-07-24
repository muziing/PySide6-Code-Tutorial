import sys

from PySide6 import QtCore, QtWidgets

"""
QAbstractSlider 追踪功能

当开启追踪功能时（默认启用），在用户拖动滑块时即发射valueChanged()信号
若关闭追踪功能，则只有在用户结束拖拽释放滑块时才发射

.setTracking(enable: bool)
.hasTracking() -> bool

当启用追踪功能时，sliderPosition等同于value
.setSliderPosition(pos: int)
.sliderPosition() -> int

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractSlider-追踪功能")
        self.resize(800, 600)
        self.setup_ui()
        self.test()

    def setup_ui(self) -> None:
        """设置界面"""

        self.slider = QtWidgets.QSlider(self)
        self.slider.move(200, 200)
        self.slider.setMaximum(200)

        info_label = QtWidgets.QLabel(self)
        info_label.move(260, 230)

        @QtCore.Slot(int)
        def show_value(value: int):
            info_label.setText(f"滑块的值变成了{value}，位置为{self.slider.sliderPosition()}")
            info_label.adjustSize()

        self.slider.valueChanged.connect(show_value)  # type: ignore

    def test(self) -> None:
        """测试滑块追踪功能"""

        # 关闭追踪功能，只有用户释放滑块后才发射valueChanged信号
        self.slider.setTracking(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
