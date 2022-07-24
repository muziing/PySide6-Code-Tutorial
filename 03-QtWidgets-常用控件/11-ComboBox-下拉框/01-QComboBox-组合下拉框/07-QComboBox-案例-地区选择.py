import sys

from PySide6 import QtWidgets

"""
QComboBox 案例：地区选择

由2个combobox组成，分别用于选择省、市，选中城市后获得对应的邮政编码

当第1个combobox的选中改变时，第2个combobox中的选项自动变换至对应列表
当第2个combobox的选中改变时，使用QLabel显示该地的邮政编码
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox-案例")
        self.resize(800, 600)

        # 创建存储城市信息的字典
        self.city_dic = {
            "北京": {
                "东城区": "100010",
                "西城区": "100032",
                "朝阳区": "100020",
                "丰台区": "100071",
                "石景山区": "100043",
                "海淀区": "100080",
            },
            "上海": {"黄浦区": "200001", "徐汇区": "200030", "长宁区": "200050"},
        }
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面并初始化"""

        self.province_cbb = QtWidgets.QComboBox()
        self.city_cbb = QtWidgets.QComboBox()
        self.code_label = QtWidgets.QLabel()

        # 使用布局管理器布局控件
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.province_cbb)
        layout.addWidget(self.city_cbb)
        layout.addWidget(self.code_label)
        self.setLayout(layout)

        # 初始化并连接信号
        self.province_cbb.addItems(self.city_dic.keys())
        self.province_cbb.currentTextChanged.connect(self.province_changed)  # type: ignore
        self.city_cbb.currentIndexChanged.connect(self.city_changed)  # type: ignore

        # 手动执行一次以为城市combobox添加初始项
        self.province_changed(self.province_cbb.currentText())

    def province_changed(self, pro_name: str) -> None:
        """
        省份改变时的槽函数 \n
        :param pro_name: 新的省名
        :return: None
        """
        # 先清空之前的条目
        self.city_cbb.clear()

        # 再添加条目
        cities = self.city_dic[pro_name]
        for city_name, city_code in cities.items():
            # 将城市名作为text、邮政代码作为data添加条目
            self.city_cbb.addItem(city_name, city_code)

    def city_changed(self, item_index: int) -> None:
        """
        城市改变时的槽函数 \n
        :param item_index: 新的选中的条目索引
        :return: None
        """
        city_name = self.city_cbb.itemText(item_index)
        city_code = self.city_cbb.itemData(item_index)
        self.code_label.setText(f"{city_name}的邮政编码为{city_code}")
        self.code_label.adjustSize()  # 调节标签控件尺寸以适应新的内容


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
