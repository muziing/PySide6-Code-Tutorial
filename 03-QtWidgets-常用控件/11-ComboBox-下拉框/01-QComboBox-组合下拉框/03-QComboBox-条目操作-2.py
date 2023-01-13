"""
QComboBox 条目操作
可以控制用户是否能够以编辑条目的方式添加新条目，以及添加新条目时的细节
亦可控制条目字符最小数量、最大条目数量、每次可见的最大条目数量等

默认情况下不允许用户编辑条目，但可以设置允许。用户编辑的条目的插入方式由插入策略控制
.setEditable(editable: bool)
.isEditable() -> bool
.setEditText(text: str)

可以控制是否允许用户添加重复的条目，默认不允许
.setDuplicatesEnabled(enable: bool)
.duplicatesEnabled() -> bool

插入策略控制着当用户创建了新的条目时该如何插入，QComboBox.InsertPolicy详情见下文
.setInsertPolicy(policy: QComboBox.InsertPolicy)
.insertPolicy() -> QComboBox.InsertPolicy

尺寸调整策略控制当内容改变时，combobox的尺寸如何改变，QComboBox.SizeAdjustPolicy详情见下文
.setSizeAdjustPolicy(policy: QComboBox.SizeAdjustPolicy)
.sizeAdjustPolicy() -> QComboBox.SizeAdjustPolicy

通过控制minimumContentsLength属性，限制最少字符数（默认为0）
.setMinimumContentsLength(characters: int)
.minimumContentsLength() -> int

还可以控制combobox中条目的最大数量（默认值为有符号整形的上限）、在屏幕上显示的最大数量（默认为10）
.setMaxCount(max: int)
.maxCount() -> int
.setMaxVisibleItems(max_items: int)
.maxVisibleItems() -> int


QComboBox.InsertPolicy 枚举值具体有如下数种：
https://doc.qt.io/qt-6/qcombobox.html#InsertPolicy-enum
QComboBox.NoInsert                  字符串不会被插入到combobox中
QComboBox.InsertAtTop               作为首条插入
QComboBox.InsertAtCurrent           替换当前条目
QComboBox.InsertAtBottom            插入到最后一条目之后
QComboBox.InsertAfterCurrent        在当前条目之后插入
QComboBox.InsertBeforeCurrent       在当前条目之前插入
QComboBox.InsertAlphabetically      按字母表顺序插入字符串至combobox

QComboBox.SizeAdjustPolicy 枚举值具体有如下数种：
https://doc.qt.io/qt-6/qcombobox.html#SizeAdjustPolicy-enum
QComboBox.AdjustToContents              总是根据内容调整尺寸
QComboBox.AdjustToContentsOnFirstShow   仅在首次出现时调整尺寸，默认值
QComboBox.AdjustToMinimumContentsLengthWithIcon
                                        将尺寸调整至最小内容长度加一个图标，出于性能原因，请在大型模型上使用此策略
"""

import sys

from PySide6 import QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox-条目操作")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        cbb = QtWidgets.QComboBox(self)
        cbb.move(300, 200)
        cbb.addItems([str(i) for i in range(100, 110)])  # 通过列表推导式快速添加多个条目

        # 允许用户编辑条目
        cbb.setEditable(True)

        # 允许用户添加重复项
        cbb.setDuplicatesEnabled(True)

        # 设置插入策略
        # cbb.setInsertPolicy(QtWidgets.QComboBoxInsertPolicy..NoInsert)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtTop)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtCurrent)
        cbb.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAfterCurrent)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertBeforeCurrent)
        # cbb.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically)

        # 设置可编辑文本
        cbb.setEditText("000")  # 将当前文本设置为00,而不影响其他条目

        # 设置尺寸调整策略
        cbb.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)  # 总是根据内容调整尺寸

        # 限制最小字符数
        cbb.setMinimumContentsLength(3)

        # 限制最大条目数，达到12条后无法再添加
        cbb.setMaxCount(12)

        # 每次只能显示5条条目，更多条目需要滚动显示
        cbb.setMaxVisibleItems(5)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
