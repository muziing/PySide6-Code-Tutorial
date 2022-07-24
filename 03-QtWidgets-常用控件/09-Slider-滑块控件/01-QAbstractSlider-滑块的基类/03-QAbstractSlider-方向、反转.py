import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

"""
QAbstractSlider 方向、反转

滑块可以设置水平、垂直两种方向
亦可设置反转值，即由原先左下为小值右上为大值，反转至右上为小值左下为大值

设置滑块方向，其中Qt.Orientation只能取Qt.Vertical垂直（默认值）或Qt.Horizontal水平两种
.setOrientation(orientation: Qt.Orientation)
.orientation() -> Qt.Orientation

设置是否开启外观反转
.setInvertedAppearance(enable: bool)
.invertedAppearance() -> bool

设置是否开启操作反转，即键鼠操作与原先相反
.setInvertedControls(enable: bool)
.invertedControls() -> bool

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

        self.slider = QtWidgets.QSlider(self)
        self.slider.move(200, 200)

        info_label = QtWidgets.QLabel(self)
        info_label.move(260, 230)

        @QtCore.Slot(int)
        def show_value(value: int):
            info_label.setText(f"滑块的值变成了{value}")
            info_label.adjustSize()

        self.slider.valueChanged.connect(show_value)  # type: ignore

    def test(self) -> None:
        """测试滑块方向、反转操作"""

        # 设置滑块方向
        # self.slider.setOrientation(Qt.Vertical)  # 垂直，默认值
        self.slider.setOrientation(Qt.Horizontal)  # 水平

        # 设置反转
        self.slider.setInvertedAppearance(True)

        # 设置操作反转
        self.slider.setInvertedControls(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
