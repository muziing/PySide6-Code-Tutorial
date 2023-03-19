"""
QPushButton 扁平化
设置扁平化后，除非按钮被按下，大部分样式不会绘制按钮背景，实现视觉上的扁平化

.setFlat(bool)     是否设置为扁平化，默认为否
.isFlat() -> bool  是否为扁平化
"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPushButton-扁平化")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        # 在此处编写设置UI的代码
        button = QtWidgets.QPushButton("扁平化的按钮", self)
        button.setFlat(True)  # 启用扁平化
        button.move(350, 200)

        print(button.isFlat())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
