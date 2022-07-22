import sys

from PySide6 import QtCore, QtGui, QtWidgets

"""
QComboBox 条目操作
提供了非常多方法来创建、插入、获取条目

添加条目
.addItem(text: str, user_data: QVariant = QVariant())
.addItem(icon: QIcon, text: str, user_data: QVariant = QVariant())
.addItems(texts: List[str])

插入条目
.insertItem(index: int, text: str, user_data: QVariant = QVariant())
.insertItem(index: int, icon: QIcon, text: str, user_data: QVariant = QVariant())
.insertItems(index: int, list: List[str])

插入分割线，在原先索引位置为index的条目之前插入，注意分割线自身也算一个条目，也会增加索引值
.insertSeparator(index: int)

设置条目属性
.setItemData(index: int, value: QVariant, role:int = Qt.UserRole)
.setItemDelegate(delegate: QAbstractItemDelegate)
.setItemIcon(index: int, icon: QIcon)
.setItemText(index: int, text: str)
.setIconSize(size: QSize)

获取条目的属性
.itemData(index: int, role: int = Qt.UserRole) -> QVariant
.itemDelegate() -> QAbstractItemDelegate
.itemIcon(index: int) -> QIcon
.itemText(index: int) -> str
.iconSize() -> QSize

移除条目
.removeItem(index: int)

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox-条目操作")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        python_icon = QtGui.QIcon("../../../Resources/Icons/Python_128px.png")
        c_icon = QtGui.QIcon("../../../Resources/Icons/C_128px.png")
        c_sharp_icon = QtGui.QIcon("../../../Resources/Icons/CSharp_128px.png")
        cpp_icon = QtGui.QIcon("../../../Resources/Icons/C++_128px.png")
        js_icon = QtGui.QIcon("../../../Resources/Icons/JavaScript_128px.png")

        cbb = QtWidgets.QComboBox(self)
        cbb.move(200, 200)
        cbb.resize(400, 60)

        # 设置图标尺寸
        cbb.setIconSize(QtCore.QSize(50, 50))

        # 添加条目
        cbb.addItem(python_icon, "Python")
        cbb.addItem("C")
        cbb.addItems(["C#", "CPP"])

        # 插入条目与分割线
        cbb.insertSeparator(1)  # 在原先索引位置为1的条目之前插入分割线，注意分割线也算一个条目
        cbb.insertItem(5, js_icon, "JavaScript")

        # 设置项目属性
        cbb.setItemIcon(2, c_icon)
        cbb.setItemIcon(3, c_sharp_icon)
        cbb.setItemIcon(4, cpp_icon)
        cbb.setItemText(4, "C++")

        # 移除条目
        cbb.removeItem(5)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
