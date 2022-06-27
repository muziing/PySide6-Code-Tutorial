import sys

from PySide6 import QtGui, QtWidgets

"""
QButtonGroup 按钮组类
官方文档：https://doc.qt.io/qtforpython/PySide6/QtWidgets/QButtonGroup.html
QButtonGroup本身也是QtWidgets下的一个类，常用于控制单选按钮的互斥性：同组内的按钮间互斥，不同组的间互不影响
更多功能请参阅文档

.__init__(self, parent: Optional[QObject] = None)     创建按钮组，父控件为可选参数
.addButton(button: QAbstractButton, id: int = -1)     将按钮添加到按钮组中，可以同时为该按钮设置id
.removeButton(button: QAbstractButton)                将按钮从按钮组中移除
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QButtonGroup-单选按钮分组")
        self.resize(800, 600)
        self.setup_ui()
        self.test_01()

    def setup_ui(self) -> None:
        """设置界面"""
        self.rb_male = QtWidgets.QRadioButton("male", self)
        self.rb_male.setIcon(
            QtGui.QIcon("../../../Resources/Icons/FlatIcon-regular-rounded/mars.png")
        )
        self.rb_male.move(250, 180)

        self.rb_female = QtWidgets.QRadioButton("female", self)
        self.rb_female.setIcon(
            QtGui.QIcon("../../../Resources/Icons/FlatIcon-regular-rounded/venus.png")
        )
        self.rb_female.move(250, 240)

        self.rb_yes = QtWidgets.QRadioButton("yes", self)
        self.rb_yes.setIcon(
            QtGui.QIcon("../../../Resources/Icons/FlatIcon-regular-rounded/check.png")
        )
        self.rb_yes.move(450, 180)

        self.rb_no = QtWidgets.QRadioButton("no", self)
        self.rb_no.setIcon(
            QtGui.QIcon("../../../Resources/Icons/FlatIcon-regular-rounded/cross.png")
        )
        self.rb_no.move(450, 240)

    def test_01(self) -> None:
        """测试按钮组"""
        gender_group = QtWidgets.QButtonGroup(self)  # 创建按钮组
        gender_group.addButton(self.rb_male)  # 将按钮添加至按钮组
        gender_group.addButton(self.rb_female)  # 处于同一组内的按钮间有互斥性

        answer_group = QtWidgets.QButtonGroup(self)
        answer_group.addButton(self.rb_yes)  # 处于不同组的按钮间没有互斥性
        answer_group.addButton(self.rb_no)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
