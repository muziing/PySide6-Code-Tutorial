import sys

from PySide6 import QtCore, QtWidgets

"""
QComboBox 信号
提供了多种精细的信号供使用

.activated(index: int)
    当用户在组合下拉框中选中一个条目时发射此信号，索引作为参数传递。即使选中项未改变也会发射
    
.currentIndexChanged(index: int)
    当当前索引由用户交互或编程方式改变时发射此信号，索引作为参数传递。
    若combobox为空或当前索引已重置，则传递条目的 index 或 -1

.currentTextChanged(text: str)
    当当前文本发生改变时发射此信号，新的值作为参数传递

.editTextChanged(text: str)
    当启用了可编辑模式，且编辑器中的文本发生改变时发射此信号，新的文本作为参数传递
    
.highlighted(index: int)
    当用户高亮（光标移入或键盘选择）了弹出菜单中的某一条目时发射此信号
    索引值作为参数传递
    
.textActivated(text: str)
    当用户选择了条目之一时，发射此信号并将文本作为参数传递
    即使选择未发生改变也会发射此信号

.textHighlighted(text: str)
    当用户高亮（光标移入或键盘选择）了弹出菜单中的某一条目时发射此信号
    文本作为参数传递

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox-信号")
        self.resize(800, 600)
        self.setup_ui()
        self.signal_test()

    def setup_ui(self) -> None:
        """设置界面"""

        self.cbb = QtWidgets.QComboBox(self)
        self.cbb.move(300, 200)
        self.cbb.addItems([str(i) for i in range(100, 105)])  # 通过列表推导式快速添加多个条目
        self.cbb.setEditable(True)  # 启用可编辑
        self.cbb.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)  # 总是根据内容调整尺寸

        self.info_label = QtWidgets.QLabel(self)
        self.info_label.move(300, 300)

    def signal_test(self) -> None:
        """测试combobox信号"""

        @QtCore.Slot(int)
        def test_index(index: int) -> None:
            """测试传递参数为索引值的信号"""
            info = f"传入的索引为{index}，该项对应的文本为{self.cbb.itemText(index)}"
            self.info_label.setText(info)
            self.info_label.adjustSize()

        @QtCore.Slot(str)
        def test_text(text: str) -> None:
            """测试传递参数为文本的信号"""
            info = f"传入的文本为{text}"
            self.info_label.setText(info)
            self.info_label.adjustSize()

        # 测试如下信号时，每次仅测试一项，注释掉其他行
        # self.cbb.activated.connect(test_index)  # type: ignore
        # self.cbb.currentIndexChanged.connect(test_index)  # type: ignore
        # self.cbb.editTextChanged.connect(test_text)  # type: ignore
        self.cbb.highlighted.connect(test_index)  # type: ignore
        # self.cbb.textActivated.connect(test_text)  # type: ignore
        # self.cbb.textHighlighted.connect(test_text)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
