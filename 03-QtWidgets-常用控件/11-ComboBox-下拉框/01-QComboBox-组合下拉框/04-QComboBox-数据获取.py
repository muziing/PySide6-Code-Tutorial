import sys

from PySide6 import QtWidgets

"""
QComboBox 数据获取
除在条目操作1中已经介绍的按索引获取条目信息外，还可以之间获取当前条目等

获取总条目数量
.count() -> int

获取条目的属性
.itemData(index: int, role: int = Qt.UserRole) -> QVariant
.itemDelegate() -> QAbstractItemDelegate
.itemIcon(index: int) -> QIcon
.itemText(index: int) -> str

获取当前条目的属性
.currentData(role: Qt.UserRole) -> QVariant
.currentIndex() -> int
.currentText() -> str

查找文本或数据，返回匹配项的索引
.findText(text: str, flags: Qt.MatchFlags) -> int
.findData(data: QVariant, role: int = Qt.UserRole, flags: Qt.MatchFlags) -> int


"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox-数据获取")
        self.resize(800, 600)
        self.setup_ui()
        self.test()

    def setup_ui(self) -> None:
        """设置界面"""
        self.cbb = QtWidgets.QComboBox(self)
        self.cbb.move(200, 200)
        self.cbb.resize(400, 60)
        self.cbb.addItems([str(i) for i in range(100, 110)])  # 通过列表推导式快速添加多个条目
        self.cbb.addItem("110", {"key": "value"})  # 将一个字典作为Data存入

    def test(self) -> None:
        """测试获取数据功能"""

        # 获取最后一项的数据
        print(f"末项数据为：{self.cbb.itemData(self.cbb.count() - 1)}")

        # 测试获取当前项的属性
        self.cbb.currentIndexChanged.connect(lambda: print(f"当前文本为：{self.cbb.currentText()}"))  # type: ignore
        self.cbb.currentIndexChanged.connect(lambda: print(f"当前数据为：{self.cbb.currentData()}"))  # type: ignore
        self.cbb.currentIndexChanged.connect(lambda: print(f"当前索引为：{self.cbb.currentIndex()}"))  # type: ignore

        # 测试查找功能
        index_102 = self.cbb.findText("102")  # 查找文本为102的项，返回找到的索引
        print(self.cbb.itemText(index_102))  # 根据索引获取该项的文本


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
