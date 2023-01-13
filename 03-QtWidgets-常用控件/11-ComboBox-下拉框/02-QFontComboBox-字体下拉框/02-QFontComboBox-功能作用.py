"""
QFontComboBox 功能作用

=========================== 显示字体 ===========================
可以指定当下拉框打开时，使用font字体显示指定的fontFamily字体族：

.setDisplayFont(font_family: str, font: QFont)  在下拉框预览中，以font字体展示font_family字体族条目

=========================== 书写系统 ===========================
可以筛选出只显示某种书写系统（拉丁语、希腊语、阿拉伯语、简体中文……）的字体
书写系统详见：https://doc.qt.io/qt-6/qfontdatabase.html#WritingSystem-enum
.setWritingSystem(writing_system: QFontDatabase.WritingSystem)
.writingSystem() -> QFontDatabase.WritingSystem

=========================== 示例文本 ===========================
可以为某些特定的字体或特定的书写系统指定示例文本，例如默认会在简体中文系统的字体后面添加“中文示例”作为
示例文本等：

.setSampleTextForFont(font_family: str, sample_text: str)
.setSampleTextForSystem(writing_system: QFontDatabase.WritingSystem, sample_text: str)
.sampleTextForFont(font_family: str) -> str
.sampleTextForSystem(writing_system: QFontDatabase.WritingSystem) -> str

=========================== 字体过滤器 ===========================
可以添加过滤器来筛选出特定类型的字体，如可缩放字体、等宽字体
QComboBox.FontFilter筛选器详见下文，多个筛选器间使用|连接即可

.setFontFilters(filters: QFontComboBox.FontFilters)
.fontFilters() -> QFontComboBox.FontFilters

QComboBox.FontFilter枚举值具体有如下取值：
https://doc.qt.io/qt-6/qfontcombobox.html#FontFilter-enum
QFontComboBox.AllFonts              显示所有字体
QFontComboBox.ScalableFonts         显示可缩放字体
QFontComboBox.NonScalableFonts      显示不可缩放字体
QFontComboBox.MonospacedFonts       显示等宽字体
QFontComboBox.ProportionalFonts     显示比例字体
"""

import sys

from PySide6 import QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QFontComboBox-功能作用")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建一个字体选择下拉框
        fcb = QtWidgets.QFontComboBox()

        # 创建示例文本并连接信号，当用户选择字体改变时，对应改变示例文本的字体
        text_label = QtWidgets.QLabel("我能吞下玻璃而不伤身体。\nThe quick brown fox jumps over the lazy dog.")
        fcb.currentFontChanged.connect(text_label.setFont)  # type: ignore

        # 使用布局管理器布局界面
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(fcb)
        layout.addWidget(text_label)
        self.setLayout(layout)

        # ======================== 设置显示字体 ========================
        fcb.setDisplayFont("Arial", QtGui.QFont("Arial Black", italic=True))  # 注意在本地测试时使用本机已安装的字体
        # 此时在combobox中的"Arial"条目是用黑体斜体显示的，而非原来的Arial字体

        # ======================== 设置示例文本、书写系统 ========================
        fcb.setSampleTextForFont("HarmonyOS Sans SC", "鸿蒙字体示例")  # 为指定字体添加示例文本

        # fcb.setWritingSystem(QtGui.QFontDatabase.SimplifiedChinese)  # 设置只显示简体中文书写系统的字体
        # 为指定文字系统（简体中文、希腊语、拉丁语、阿拉伯语……）添加示例文本
        fcb.setSampleTextForSystem(
            QtGui.QFontDatabase.WritingSystem.SimplifiedChinese, "我能吞下玻璃而不伤身体。"
        )
        fcb.setSampleTextForSystem(
            QtGui.QFontDatabase.WritingSystem.TraditionalChinese, "我能吞下玻璃而不傷身體。"
        )
        # 获取示例文本
        print(fcb.sampleTextForSystem(QtGui.QFontDatabase.WritingSystem.SimplifiedChinese))
        print(fcb.sampleTextForSystem(QtGui.QFontDatabase.WritingSystem.Arabic))

        # ======================== 设置字体筛选器 ========================
        # 筛选出等宽且不可缩放的字体
        # fcb.setFontFilters(
        #     QtWidgets.QFontComboBox.MonospacedFonts | QtWidgets.QFontComboBox.NonScalableFonts
        # )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
