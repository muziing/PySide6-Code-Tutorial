import sys

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

"""
QWidget 光标
可以自定义光标形状、获取光标位置等
控件默认使用箭头形状光标，Qt还内置提供了许多光标形状（参下方Qt.CursorShape），也可以使用位图自定义光标形状
子控件默认使用与父控件相同的光标形状，也可以单独设置

QWidget.setCursor(QCursor)   设置光标形状
QWidget.unsetCursor()        取消设置光标形状
QWidget.cursor() -> QCursor  获取光标形状


QCursor 类的常用方法：
QCursor.__init__(shape: Qt.CursorShape)      使用Qt内置的光标形状创建
QCursor.__init__(pixmap: Union[QPixmap, QImage, str], hotX: int = -1, hotY: int = -1)    使用QPixmap位图创建
QCursor.pos() -> QPoint                      返回该光标当前所在位置坐标（相对于整个屏幕）
QCursor.setPos(QPoint)                       设置光标位置坐标（相对于屏幕）


Qt.CursorShape 具体分为二十余种，详细信息请参阅文档，以下列举几种
https://doc.qt.io/qt-6/qt.html#CursorShape-enum
Qt.ArrowCursor       标准的箭头光标
Qt.WaitCursor        沙漏或手表光标，通常在阻止用户与应用程序交互的操作期间显示
Qt.IBeamCursor       插入符号或工字形光标，表示控件可以接受并显示文本输入
Qt.SizeFDiagCursor   用于对角调整顶级窗口左上角和右下角大小的元素的光标
Qt.ForbiddenCursor   一种斜线圆圈光标，通常在拖放操作期间使用，以指示拖放的内容不能放在特定控件上或放在特定区域内
Qt.BusyCursor        沙漏或手表光标，通常在操作期间显示，这些操作允许用户在后台执行时与应用程序进行交互

关于 QCursor 类的更多信息请参阅本项目QtGui目录下的对应目录，以及官方文档
https://doc.qt.io/qt-6/qcursor.html
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QWidget-光标")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()
        self.test_02()

    def setup_ui(self) -> None:
        """设置界面"""
        self.label = QtWidgets.QLabel(self)
        self.label.resize(300, 300)
        self.label.setStyleSheet("background-color: cyan;")
        self.button = QtWidgets.QPushButton("测试按钮", self)
        self.button.move(350, 200)

    def test_01(self) -> None:
        """测试设置光标"""

        # 设置为自定义图案光标
        pixmap = QtGui.QPixmap("../../Resources/Icons/snowflake_128px.ico").scaled(52, 52)
        my_cursor = QtGui.QCursor(pixmap, 26, 26)  # 以图片像素点位置26,26为热点（光标实际所在位置坐标）
        self.setCursor(my_cursor)

        # 设置label中的光标为Qt内置的其他光标
        self.label.setCursor(Qt.ForbiddenCursor)
        # self.label.setCursor(Qt.OpenHandCursor)

    def test_02(self) -> None:
        """测试获取光标"""

        current_cursor = self.cursor()
        self.button.clicked.connect(lambda: print(current_cursor.pos()))  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
