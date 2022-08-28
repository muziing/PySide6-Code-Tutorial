import sys

from PySide6 import QtCore, QtWidgets

"""
QDateTimeEdit 日期时间编辑器

用于接收用户输入的日期、时间
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDateTimeEdit.html
继承自QAbstractSpinBox
其下有QDateEdit、QTimeEdit两个子类，功能与QDateTimeEdit中的完全一致，只是做了拆分

有如下数种构造函数，可以在创建时传入QDate/QTime/QDateTime,也可选地指定父控件
.__init__(self, parent: Optional[QtWidgets.QWidget] = None)
.__init__(self, d: QtCore.QDate, parent: Optional[QtWidgets.QWidget] = None)
.__init__(self, t: QtCore.QTime, parent: Optional[QtWidgets.QWidget] = None)
.__init__(self, dt: QtCore.QDateTime, parent: Optional[QtWidgets.QWidget] = None)


"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QDateTimeEdit")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        my_time = QtCore.QTime(16, 30, 0, 0)
        my_date = QtCore.QDate.currentDate()

        # dte = QtWidgets.QDateTimeEdit(self)  # 创建空的日期时间编辑器
        # dte = QtWidgets.QDateTimeEdit(my_time, self)  # 使用QTime初始化
        # dte = QtWidgets.QDateTimeEdit(my_date, self)  # 使用QDate初始化
        dte = QtWidgets.QDateTimeEdit(QtCore.QDateTime.currentDateTime(), self)  # 使用QDateTime初始化

        dte.move(200, 200)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
