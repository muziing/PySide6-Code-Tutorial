import sys

from PySide6 import QtWidgets

"""
QAbstractSlider 信号

actionTriggered(action: int)      当action被触发时发射此信号，详情参考文档
rangeChanged(min: int, max: int)  当滑块数值范围变化时发射此信号，新的最小/大值作为参数传递
sliderMoved(value: int)           当滑块被按下并移动时发射此信号，新的位置作为参数传递
sliderPressed()                   当滑块被用户按下或编程按下时发射此信号
sliderReleased()                  当滑块被用户释放或编程释放时发射此信号
valueChanged(value: int)          当滑块的值改变时发射此信号，新的值作为参数传出

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractSlider-信号")
        self.resize(800, 600)
        self.slider = QtWidgets.QSlider(self)
        self.setup_ui()
        self.signal_test()

    def setup_ui(self) -> None:
        """设置界面"""

        self.slider.move(200, 200)

    def signal_test(self) -> None:
        """测试滑块的各种信号"""

        self.slider.sliderMoved.connect(lambda value: print(f"滑块移动到了{value}"))  # type: ignore
        self.slider.sliderPressed.connect(lambda: print("滑块被按下了！"))  # type: ignore
        self.slider.sliderReleased.connect(lambda: print("滑块被释放了！"))  # type: ignore
        self.slider.valueChanged.connect(lambda value: print(f"滑块的值变成了了{value}"))  # type: ignore
        self.slider.rangeChanged.connect(lambda min_, max_: print(f"滑块的最小值变为了{min_}，最大值变为{max_}"))  # type: ignore

        self.slider.setMaximum(200)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
