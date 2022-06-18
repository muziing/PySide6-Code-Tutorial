import sys

from PySide6 import QtWidgets

"""
QAbstractButton 自动重复

按钮可以设置自动重复，按下不放时反复发射 pressed() released() clicked() 信号
推荐阅读：https://doc.qt.io/qt-6/qabstractbutton.html#autoRepeat-prop

.setAutoRepeat(bool)          设置是否开启自动重复，默认关闭
.setAutoRepeatDelay(int)      设置触发自动重复的延时，即按住多长时间后才开始自动重复，单位为毫秒
.setAutoRepeatInterval(int)   设置自动重复的时间间隔，单位为毫秒
.autoRepeat() -> bool         获取自动重复状态
.autoRepeatDelay() -> int     获取自动重复延时，单位毫秒
.autoRepeatInterval() -> int  获取自动重复时间间隔，单位毫秒
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QAbstractButton-自动重复")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        # 由于QAbstractButton是抽象类不能被实例化，使用QPushButton演示
        button = QtWidgets.QPushButton("按钮自动重复", self)
        button.move(350, 200)
        button.clicked.connect(lambda: print("按钮被点击了"))  # type: ignore

        # 设置自动重复
        button.setAutoRepeat(True)  # 启用自动重复
        button.setAutoRepeatDelay(1000)  # 按住按钮1秒才开始自动重复
        button.setAutoRepeatInterval(300)  # 每300毫秒重复一次

        # 当按住按钮不放超过1秒后，按钮自动反复发射clicked等信号，松开按钮后停止

        print(button.autoRepeat())
        print(button.autoRepeatDelay())
        print(button.autoRepeatInterval())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
