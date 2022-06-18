import sys

from PySide6 import QtCore, QtGui, QtWidgets

"""
QPushButton 菜单

可以将普通按钮添加菜单而使其成为菜单按钮，一个按钮可以实现多个功能
建议参考：https://doc.qt.io/qt-6/qpushbutton.html#setMenu
关于 QMenu 详细用法，请查阅本项目对应目录

.setMenu(menu: QMenu)  为按钮设置菜单
.Menu() -> QMenu       获取按钮的菜单
.showMenu()            槽函数：打开按钮的菜单
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QPushButton-菜单")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        button = QtWidgets.QPushButton("菜单按钮", self)
        button.move(350, 200)

        # --------------创建并配置菜单------------------------------
        test_menu = QtWidgets.QMenu(self)  # 创建一个菜单

        new_action = QtGui.QAction("新建", test_menu)  # 创建 action
        new_action.triggered.connect(lambda: print("新建文件"))  # type: ignore
        exit_action = QtGui.QAction("关闭", test_menu)
        exit_action.triggered.connect(lambda: exit())  # type: ignore

        # 创建一个子菜单
        open_url_menu = QtWidgets.QMenu("打开网页")
        url_action_1 = QtGui.QAction("PySide6 Code Tutorial", open_url_menu)
        url_action_2 = QtGui.QAction("muzing 的博客", open_url_menu)
        blog_url = QtCore.QUrl("https://muzing.top")
        project_url = QtCore.QUrl("https://github.com/muziing/PySide6-Code-Tutorial")
        url_action_1.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(project_url))  # type: ignore
        url_action_2.triggered.connect(lambda: QtGui.QDesktopServices.openUrl(blog_url))  # type: ignore
        open_url_menu.addAction(url_action_1)
        open_url_menu.addAction(url_action_2)

        # 将actions、子菜单、分割线添加到菜单
        test_menu.addAction(new_action)
        test_menu.addMenu(open_url_menu)  # 将一个菜单添加到另一个菜单中，即成为子菜单
        test_menu.addSeparator()  # 添加分割线
        test_menu.addAction(exit_action)

        # ----------------------------------------------------------

        # 为按钮设置菜单
        button.setMenu(test_menu)

        button_2 = QtWidgets.QPushButton("展开菜单", self)
        button_2.move(350, 150)
        # button2的点击信号连接到button的展示按钮槽
        button_2.clicked.connect(button.showMenu)  # type: ignore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
