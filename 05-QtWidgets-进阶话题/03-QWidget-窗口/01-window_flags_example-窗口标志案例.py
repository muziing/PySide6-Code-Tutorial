import sys
from typing import Type

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

"""
本案例为 Qt 官方案例 Window Flags Example 的 PySide6 移植版
https://doc.qt.io/qt-6/qtwidgets-widgets-windowflags-example.html

用于展示在不同的 Window Flags 标记下，顶层窗口的样式状态
https://doc.qt.io/qt-6/qt.html#WindowType-enum
"""


class ControllerWindow(QtWidgets.QWidget):
    """控制窗口类"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.preview_window = PreviewWindow(self)  # 创建预览窗口

        self.create_type_groupbox()
        self.create_hints_groupbox()

        quit_button = QtWidgets.QPushButton("Quit")
        quit_button.clicked.connect(QtCore.QCoreApplication.quit)  # type: ignore

        bottom_layout = QtWidgets.QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(quit_button)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.type_groupbox)
        main_layout.addWidget(self.hints_group_box)
        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)

        self.setWindowTitle("Window Flags")
        self.update_preview()

    def create_type_groupbox(self) -> None:
        """
        创建type单选按钮，并布局到组框中 \n
        :return: None
        """

        self.type_groupbox = QtWidgets.QGroupBox("Type")

        self.window_radiobutton = self.crate_radiobutton("Window")
        self.dialog_radiobutton = self.crate_radiobutton("Dialog")
        self.sheet_radiobutton = self.crate_radiobutton("Sheet")
        self.popup_radiobutton = self.crate_radiobutton("Popup")
        self.tool_radiobutton = self.crate_radiobutton("Tool")
        self.tool_tip_radiobutton = self.crate_radiobutton("Tooltip")
        self.splash_screen_radiobutton = self.crate_radiobutton("Splash screen")
        self.sub_window_radiobutton = self.crate_radiobutton("Sub window")
        self.foreign_window_radiobutton = self.crate_radiobutton("Foreign window")
        self.cover_window_radiobutton = self.crate_radiobutton("Cover window")
        self.window_radiobutton.setChecked(True)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.window_radiobutton, 0, 0)
        layout.addWidget(self.dialog_radiobutton, 1, 0)
        layout.addWidget(self.sheet_radiobutton, 2, 0)
        layout.addWidget(self.popup_radiobutton, 3, 0)
        layout.addWidget(self.tool_radiobutton, 4, 0)
        layout.addWidget(self.tool_tip_radiobutton, 0, 1)
        layout.addWidget(self.splash_screen_radiobutton, 1, 1)
        layout.addWidget(self.sub_window_radiobutton, 2, 1)
        layout.addWidget(self.foreign_window_radiobutton, 3, 1)
        layout.addWidget(self.cover_window_radiobutton, 4, 1)
        self.type_groupbox.setLayout(layout)

    def create_hints_groupbox(self) -> None:
        """
        创建hints复选框，并布局到组框中 \n
        :return: None
        """

        self.hints_group_box = QtWidgets.QGroupBox("Hints")

        self.ms_windows_fixed_size_dialog_checkbox = self.create_checkbox(
            "MS Windows fixed size dialog"
        )
        self.bypass_window_manager_checkbox = self.create_checkbox("Bypass window manager")
        self.x11_bypass_window_manager_checkbox = self.create_checkbox("X11 bypass window manager")
        self.frameless_window_check_box = self.create_checkbox("Frameless window")
        self.window_no_shadow_check_box = self.create_checkbox("No drop shadow")
        self.window_title_check_box = self.create_checkbox("Window title")
        self.window_system_menu_check_box = self.create_checkbox("Window system menu")
        self.window_minimize_button_check_box = self.create_checkbox("Window minimize button")
        self.window_maximize_button_check_box = self.create_checkbox("Window maximize button")
        self.window_close_button_check_box = self.create_checkbox("Window close button")
        self.window_context_help_button_check_box = self.create_checkbox(
            "Window context help button"
        )
        self.window_shade_button_check_box = self.create_checkbox("Window shade button")
        self.window_stays_on_top_check_box = self.create_checkbox("Window stays on top")
        self.window_stays_on_bottom_check_box = self.create_checkbox("Window stays on bottom")
        self.customize_window_hint_check_box = self.create_checkbox("Customize window")
        self.window_transparent_for_input_check_box = self.create_checkbox(
            "Window transparent for input"
        )
        self.ms_windows_own_dc_check_box = self.create_checkbox("MS Windows own DC")
        self.max_using_full_screen_hint_check_box = self.create_checkbox(
            "Maximize using full screen"
        )

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.ms_windows_fixed_size_dialog_checkbox, 0, 0)
        layout.addWidget(self.ms_windows_own_dc_check_box, 1, 0)
        layout.addWidget(self.bypass_window_manager_checkbox, 2, 0)
        layout.addWidget(self.x11_bypass_window_manager_checkbox, 3, 0)
        layout.addWidget(self.frameless_window_check_box, 4, 0)
        layout.addWidget(self.window_no_shadow_check_box, 5, 0)
        layout.addWidget(self.customize_window_hint_check_box, 6, 0)
        layout.addWidget(self.window_title_check_box, 7, 0)
        layout.addWidget(self.window_system_menu_check_box, 8, 0)
        layout.addWidget(self.window_minimize_button_check_box, 0, 1)
        layout.addWidget(self.window_maximize_button_check_box, 1, 1)
        layout.addWidget(self.window_close_button_check_box, 2, 1)
        layout.addWidget(self.window_context_help_button_check_box, 3, 1)
        layout.addWidget(self.window_stays_on_top_check_box, 4, 1)
        layout.addWidget(self.window_shade_button_check_box, 5, 1)
        layout.addWidget(self.window_stays_on_bottom_check_box, 6, 1)
        layout.addWidget(self.window_transparent_for_input_check_box, 7, 1)
        layout.addWidget(self.max_using_full_screen_hint_check_box, 8, 1)

        self.hints_group_box.setLayout(layout)

    def update_preview(self) -> None:
        """
        为preview窗口设置新的flags并重新显示
        :return: None
        """

        flags: Type[Qt.WindowFlags] = Qt.WindowFlags

        if self.window_radiobutton.isChecked():
            flags = Qt.Window
        elif self.dialog_radiobutton.isChecked():
            flags = Qt.Dialog
        elif self.sheet_radiobutton.isChecked():
            flags = Qt.Sheet
        elif self.popup_radiobutton.isChecked():
            flags = Qt.Popup
        elif self.tool_radiobutton.isChecked():
            flags = Qt.Tool
        elif self.tool_tip_radiobutton.isChecked():
            flags = Qt.ToolTip
        elif self.splash_screen_radiobutton.isChecked():
            flags = Qt.SplashScreen
        elif self.sub_window_radiobutton.isChecked():
            flags = Qt.SubWindow
        elif self.foreign_window_radiobutton.isChecked():
            flags = Qt.ForeignWindow
        elif self.cover_window_radiobutton.isChecked():
            flags = Qt.CoverWindow

        if self.ms_windows_fixed_size_dialog_checkbox.isChecked():
            flags |= Qt.MSWindowsFixedSizeDialogHint
        if self.bypass_window_manager_checkbox.isChecked():
            flags |= Qt.BypassWindowManagerHint
        if self.x11_bypass_window_manager_checkbox.isChecked():
            flags |= Qt.X11BypassWindowManagerHint
        if self.frameless_window_check_box.isChecked():
            flags |= Qt.FramelessWindowHint
        if self.window_no_shadow_check_box.isChecked():
            flags |= Qt.NoDropShadowWindowHint
        if self.window_title_check_box.isChecked():
            flags |= Qt.WindowTitleHint
        if self.window_system_menu_check_box.isChecked():
            flags |= Qt.WindowSystemMenuHint
        if self.window_minimize_button_check_box.isChecked():
            flags |= Qt.WindowMinimizeButtonHint
        if self.window_maximize_button_check_box.isChecked():
            flags |= Qt.WindowMaximizeButtonHint
        if self.window_close_button_check_box.isChecked():
            flags |= Qt.WindowCloseButtonHint
        if self.window_context_help_button_check_box.isChecked():
            flags |= Qt.WindowContextHelpButtonHint
        if self.window_shade_button_check_box.isChecked():
            flags |= Qt.WindowShadeButtonHint
        if self.window_stays_on_top_check_box.isChecked():
            flags |= Qt.WindowStaysOnTopHint
        if self.window_stays_on_bottom_check_box.isChecked():
            flags |= Qt.WindowStaysOnBottomHint
        if self.customize_window_hint_check_box.isChecked():
            flags |= Qt.CustomizeWindowHint
        if self.window_transparent_for_input_check_box.isChecked():
            flags |= Qt.WindowTransparentForInput
        if self.ms_windows_own_dc_check_box.isChecked():
            flags |= Qt.MSWindowsOwnDC
        if self.max_using_full_screen_hint_check_box.isChecked():
            flags |= Qt.MaximizeUsingFullscreenGeometryHint

        self.preview_window.set_window_flags(flags)

        # 防止某些平台下窗口出现在不可见的位置
        pos = self.preview_window.pos()
        if pos.x() < 0:
            pos.setX(0)
        if pos.y() < 0:
            pos.setY(0)
        self.preview_window.move(pos)
        self.preview_window.show()  # 重新显示preview窗口

    def crate_radiobutton(self, text: str) -> QtWidgets.QRadioButton:
        """
        快速创建单选按钮并连接clicked信号至self.update_preview槽函数 \n
        :param text: 单选按钮的文字
        :return: 创建的单选按钮
        """
        button = QtWidgets.QRadioButton(text)
        button.clicked.connect(self.update_preview)  # type: ignore
        return button

    def create_checkbox(self, text: str) -> QtWidgets.QCheckBox:
        """
        快速创建复选框并连接clicked信号至self.update_preview槽函数 \n
        :param text: 复选框的文字
        :return: 创建的复选框
        """
        checkbox = QtWidgets.QCheckBox(text)
        checkbox.clicked.connect(self.update_preview)  # type: ignore
        return checkbox


class PreviewWindow(QtWidgets.QWidget):
    """预览窗口类"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 创建一个只读的文本编辑器，用于显示当前窗口状态
        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

        self.close_button = QtWidgets.QPushButton("&Close")
        self.close_button.clicked.connect(self.close)  # type: ignore

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

        self.setWindowTitle("Preview")

    def set_window_flags(self, flags: Qt.WindowFlags) -> None:
        """
        设置窗口标志并显示到文本编辑器中 \n
        :param flags: 窗口标记
        :return: None
        """

        self.setWindowFlags(flags)

        text = ""  # 用于在窗口显示的提示文本
        window_type = flags & Qt.WindowType_Mask

        # 设置窗口类型的提示文本
        if window_type == Qt.Window:
            text = "Qt.Window"
        elif window_type == Qt.Dialog:
            text = "Qt.Dialog"
        elif window_type == Qt.Sheet:
            text = "Qt.Sheet"
        elif window_type == Qt.Drawer:
            text = "Qt.Drawer"
        elif window_type == Qt.Popup:
            text = "Qt.Popup"
        elif window_type == Qt.Tool:
            text = "Qt.Tool"
        elif window_type == Qt.ToolTip:
            text = "Qt.ToolTip"
        elif window_type == Qt.SplashScreen:
            text = "Qt.SplashScreen"
        elif window_type == Qt.SubWindow:
            text = "Qt.SubWindow"
        elif window_type == Qt.ForeignWindow:
            text = "Qt.ForeignWindow"
        elif window_type == Qt.CoverWindow:
            text = "Qt.CoverWindow"

        # 设置窗口标志的提示文本
        if flags & Qt.MSWindowsFixedSizeDialogHint:
            text += "\n|  Qt.MSWindowsFixedSizeDialogHint"
        if flags & Qt.BypassWindowManagerHint:
            text += "\n|  Qt.BypassWindowManagerHint"
        if flags & Qt.X11BypassWindowManagerHint:
            text += "\n|  Qt.X11BypassWindowManagerHint"
        if flags & Qt.FramelessWindowHint:
            text += "\n|  Qt.FramelessWindowHint"
        if flags & Qt.NoDropShadowWindowHint:
            text += "\n|  Qt.NoDropShadowWindowHint"
        if flags & Qt.WindowTitleHint:
            text += "\n|  Qt.WindowTitleHint"
        if flags & Qt.WindowSystemMenuHint:
            text += "\n|  Qt.WindowSystemMenuHint"
        if flags & Qt.WindowMinimizeButtonHint:
            text += "\n|  Qt.WindowMinimizeButtonHint"
        if flags & Qt.WindowMaximizeButtonHint:
            text += "\n|  Qt.WindowMaximizeButtonHint"
        if flags & Qt.WindowCloseButtonHint:
            text += "\n|  Qt.WindowCloseButtonHint"
        if flags & Qt.WindowContextHelpButtonHint:
            text += "\n|  Qt.WindowContextHelpButtonHint"
        if flags & Qt.WindowShadeButtonHint:
            text += "\n|  Qt.WindowShadeButtonHint"
        if flags & Qt.WindowStaysOnTopHint:
            text += "\n|  Qt.WindowStaysOnTopHint"
        if flags & Qt.WindowStaysOnBottomHint:
            text += "\n|  Qt.WindowStaysOnBottomHint"
        if flags & Qt.CustomizeWindowHint:
            text += "\n|  Qt.CustomizeWindowHint"
        if flags & Qt.WindowTransparentForInput:
            text += "\n|  Qt.WindowTransparentForInput"
        if flags & Qt.MSWindowsOwnDC:
            text += "\n|  Qt.MSWindowsOwnDC"
        if flags & Qt.MaximizeUsingFullscreenGeometryHint:
            text += "\n|  Qt.MaximizeUsingFullscreenGeometryHint"

        self.text_edit.setPlainText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ControllerWindow()
    window.show()
    sys.exit(app.exec())
