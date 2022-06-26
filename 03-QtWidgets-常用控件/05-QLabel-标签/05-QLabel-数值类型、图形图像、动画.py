import sys

from PySide6 import QtGui, QtWidgets

"""
QLabel 数值类型、图形图像、动画
QLabel除了显示文本字符串外，还可以用于显示数值类型、图形图像、动图等

.setNum(num: int)                将标签设置为数值类型（int）
.setNum(num: float)              将标签设置为数值类型（float）
.setPicture(picture: QPicture)   设置标签显示的图像
.picture() -> QPicture           获取标签显示的图像
.setPixmap(p: QPixmap)           设置标签显示的位图
.pixmap() -> QPixmap             获取标签显示的位图
.setMovie(movie: QMovie)         设置标签显示的动画
.movie -> QMovie                 获取标签显示的动画

关于QPixmap、QPicture、QMovie的更多信息，请参考本项目QtGui目录
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLabel-显示非文本内容")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # ============ 数值类型 =============
        label_1 = QtWidgets.QLabel(self)
        label_1.move(320, 100)
        label_1.setNum(666)  # 设置为数值类型
        # label_1.setNum(88.8)  # 也可以设置浮点数

        # ============= 图像 ================
        label_2 = QtWidgets.QLabel(self)
        pic = QtGui.QPicture()  # 创建绘画设备（画布）
        painter = QtGui.QPainter(pic)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 128, 128)))  # 设置画刷
        painter.drawEllipse(0, 0, 150, 150)  # 绘制椭圆
        painter.end()
        label_2.setPicture(pic)  # 用于展示QPicture

        # ============= 位图 ================
        label_3 = QtWidgets.QLabel(self)
        label_3.move(600, 0)
        label_3.setPixmap(QtGui.QPixmap("../../Resources/Icons/OS_Ubuntu_128px.ico"))

        # ============= 动画 ================
        label_4 = QtWidgets.QLabel(self)
        label_4.move(200, 200)
        movie = QtGui.QMovie("../../Resources/Images/loading.gif")
        label_4.setMovie(movie)
        movie.start()  # 开始播放
        # movie.setPaused(True)  # 暂停播放


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
