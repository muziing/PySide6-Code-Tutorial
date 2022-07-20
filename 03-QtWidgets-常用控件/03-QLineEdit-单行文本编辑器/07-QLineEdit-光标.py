import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

"""
QLineEdit 光标相关


.cursorForward(mark: bool, steps: int = 1)    将光标向前移动steps更个字符
.cursorBackward(mark: bool, steps: int = 1)   将光标向后移动steps个字符
.cursorWordForward(mark: bool)                将光标向前移动一个单词
.cursorWordBackward(mark: bool)               将光标向后移动一个单词
以上四种方法，若mark参数为True,则光标移动时将把经过的范围加入选中，
若为False则清除选中


.setCursorPosition(int)                       设置光标位置
.cursorPosition() -> int                      获取光标位置
.cursorPositionAt(pos: QPoint) -> int         返回在pos位置(二维坐标)的光标位置(行编辑器内的位置)


.setCursorMoveStyle(Qt.CursorMoveStyle)       设置光标移动方式，Qt.CursorMoveStyle详情见下文
.cursorMoveStyle() -> Qt.CursorMoveStyle      返回光标移动方式

Qt.CursorMoveStyle枚举值具体有如下两种值：
https://doc.qt.io/qt-6/qt.html#CursorMoveStyle-enum
逻辑风格中，键盘左箭头意味着光标向文本的前方移动（对于从右至左的文本，前方意味着右方）；
而视觉风格中，键盘左箭头意味着光标向视觉上的左侧移动，而不考虑文本书写方向。
Qt.LogicalMoveStyle                           逻辑风格
Qt.VisualMoveStyle                            视觉风格

"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QLineEdit-光标")
        self.resize(600, 400)
        self.setup_ui()
        self.test_cursor()

    def setup_ui(self) -> None:
        """设置界面"""

        # 主要测试对象：line_edit
        self.line_edit = QtWidgets.QLineEdit()

        # ================ 移动光标 =======================
        move_groupbox = QtWidgets.QGroupBox("移动光标")
        self.move_step_length_checkbox = QtWidgets.QCheckBox("以单词为单位移动")
        self.move_flag_checkbox = QtWidgets.QCheckBox("移动时选中文本")
        self.cursor_forward_button = QtWidgets.QPushButton("向前移动")
        self.cursor_backward_button = QtWidgets.QPushButton("向后移动")

        move_layout = QtWidgets.QVBoxLayout()
        move_layout.addWidget(self.move_step_length_checkbox)
        move_layout.addWidget(self.move_flag_checkbox)
        move_layout.addWidget(self.cursor_forward_button)
        move_layout.addWidget(self.cursor_backward_button)
        move_groupbox.setLayout(move_layout)

        # ================ 光标位置 =======================
        pos_groupbox = QtWidgets.QGroupBox("光标位置")
        self.pos_line_edit = QtWidgets.QLineEdit()
        self.pos_line_edit.setReadOnly(True)
        self.set_pos_spinbox = QtWidgets.QSpinBox()
        self.set_pos_spinbox.setRange(0, 200)
        self.pos_at_label = QtWidgets.QLabel()

        self.point = QtCore.QPoint(80, 20)

        pos_layout = QtWidgets.QFormLayout()
        pos_layout.addRow(QtWidgets.QLabel("光标当前位于："), self.pos_line_edit)
        pos_layout.addRow(QtWidgets.QLabel("将光标设置到："), self.set_pos_spinbox)
        pos_layout.addRow(QtWidgets.QLabel(f"{self.point.toTuple()}处的光标位于"), self.pos_at_label)
        pos_groupbox.setLayout(pos_layout)

        # ================ 光标移动风格 =======================
        move_style_groupbox = QtWidgets.QGroupBox("光标移动风格")
        self.toward_switch_checkbox = QtWidgets.QCheckBox("切换文本方向")
        self.logical_move_radio = QtWidgets.QRadioButton("逻辑移动风格")
        self.visual_move_radio = QtWidgets.QRadioButton("视觉移动风格")

        move_style_layout = QtWidgets.QVBoxLayout()
        move_style_layout.addWidget(self.toward_switch_checkbox)
        move_style_layout.addWidget(self.logical_move_radio)
        move_style_layout.addWidget(self.visual_move_radio)
        move_style_groupbox.setLayout(move_style_layout)

        # ================ 总布局 =======================
        bottom_layout = QtWidgets.QHBoxLayout()
        bottom_layout.addWidget(move_groupbox)
        bottom_layout.addWidget(pos_groupbox)
        bottom_layout.addWidget(move_style_groupbox)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.line_edit)
        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)

    def test_cursor(self):
        """测试光标相关功能"""

        # ================ 移动光标 =======================
        @QtCore.Slot()
        def cursor_move_forward():
            """以指定的方式向前移动光标"""
            mark = self.move_flag_checkbox.isChecked()
            if self.move_step_length_checkbox.isChecked():
                self.line_edit.cursorWordForward(mark)
            else:
                self.line_edit.cursorForward(mark)
            self.line_edit.setFocus()

        @QtCore.Slot()
        def cursor_move_backward():
            """以指定的方式向后移动光标"""
            mark = self.move_flag_checkbox.isChecked()
            if self.move_step_length_checkbox.isChecked():
                self.line_edit.cursorWordBackward(mark)
            else:
                self.line_edit.cursorBackward(mark)
            self.line_edit.setFocus()

        # 连接信号与槽
        self.cursor_forward_button.clicked.connect(cursor_move_forward)  # type: ignore
        self.cursor_backward_button.clicked.connect(cursor_move_backward)  # type: ignore

        # ================ 光标位置 =======================
        @QtCore.Slot()
        def show_cursor_pos():
            """在pos_line_edit中展示当前line_edit中光标的位置"""
            self.pos_line_edit.setText(str(self.line_edit.cursorPosition()))

        @QtCore.Slot(int)
        def move_cursor_pos(pos):
            """将line_edit的光标设置为set_pos_spinbox中的数值"""
            self.line_edit.setCursorPosition(pos)
            self.line_edit.setFocus()

        @QtCore.Slot()
        def update_pos_at_label():
            self.pos_at_label.setText(f"{self.line_edit.cursorPositionAt(self.point)}")

        # 连接信号与槽
        self.line_edit.cursorPositionChanged.connect(show_cursor_pos)  # type: ignore
        self.set_pos_spinbox.valueChanged[int].connect(move_cursor_pos)  # type: ignore
        self.line_edit.cursorPositionChanged.connect(update_pos_at_label)  # type: ignore

        # ================ 光标移动风格 =======================

        # 目前通过指定setLayoutDirection的方法改变单行编辑器中文本方向的方式已不再可用
        @QtCore.Slot(bool)
        def change_toward(yes: bool):
            """改变单行编辑器中文本方向"""
            if yes:
                self.line_edit.setLayoutDirection(Qt.RightToLeft)
                self.line_edit.setText("مرحبا بالعالم.")
            else:
                self.line_edit.setLayoutDirection(Qt.LeftToRight)
                self.line_edit.setText("Hello world.")
            self.line_edit.setFocus()

        @QtCore.Slot()
        def set_logical_move():
            """将光标移动方式设置为逻辑风格"""
            self.line_edit.setCursorMoveStyle(Qt.LogicalMoveStyle)
            self.line_edit.setFocus()

        @QtCore.Slot()
        def set_visual_move():
            """将光标移动方式设置为视觉风格"""
            self.line_edit.setCursorMoveStyle(Qt.VisualMoveStyle)
            self.line_edit.setFocus()

        # 连接信号与槽
        self.toward_switch_checkbox.toggled[bool].connect(change_toward)  # type: ignore
        self.logical_move_radio.clicked.connect(set_logical_move)  # type: ignore
        self.visual_move_radio.clicked.connect(set_visual_move)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
