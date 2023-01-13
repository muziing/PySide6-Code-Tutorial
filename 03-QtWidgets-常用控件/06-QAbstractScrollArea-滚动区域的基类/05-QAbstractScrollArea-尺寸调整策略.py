"""
QAbstractScrollArea  尺寸调整策略
可以控制当视口尺寸改变时，滚动区域的尺寸如何调整的策略

.setSizeAdjustPolicy(policy: QAbstractScrollArea.SizeAdjustPolicy)  设置尺寸调整策略
.sizeAdjustPolicy() -> QAbstractScrollArea.SizeAdjustPolicy         获取尺寸调整策略

QAbstractScrollArea.SizeAdjustPolicy枚举值具体有如下三种：
https://doc.qt.io/qt-6/qabstractscrollarea.html#SizeAdjustPolicy-enum
QAbstractScrollArea.AdjustIgnored                   滚动区域行为与之前相同，不做任何调整（默认值）
QAbstractScrollArea.AdjustToContents                滚动区域总是根据视口调整尺寸
QAbstractScrollArea.AdjustToContentsOnFirstShow     滚动区域首次出现时根据视口调整尺寸
"""

import sys

from PySide6 import QtGui, QtWidgets


class MyWidget(QtWidgets.QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractScrollArea-尺寸调整策略")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()

    def setup_ui(self) -> None:
        """设置界面"""
        image_label = QtWidgets.QLabel(self)
        image_label.setPixmap(QtGui.QPixmap("../../Resources/Images/Python-code.jpg"))
        self.setWidget(image_label)

    def test_01(self) -> None:
        """测试尺寸调整策略功能"""
        # self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        # self.setSizeAdjustPolicy(
        #     QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow
        # )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
