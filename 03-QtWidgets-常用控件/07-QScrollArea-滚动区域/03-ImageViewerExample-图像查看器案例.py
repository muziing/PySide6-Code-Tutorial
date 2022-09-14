import sys
from typing import List

from PySide6.QtCore import QDir, QMimeData, QStandardPaths
from PySide6.QtGui import *
from PySide6.QtWidgets import *

"""
Image Viewer Example 图像查看器案例
本案例为Qt官方同名案例的PySide6移植版，结合QLabel与QScrollArea实现图像显示功能
https://doc.qt.io/qt-6/qtwidgets-widgets-imageviewer-example.html

注意本脚本仍有部分函数未能完全完成改写

"""


def clipboard_image() -> QImage:
    mime_data: QMimeData = QMimeData()
    if mime_data == QGuiApplication.clipboard().mimeData():
        if mime_data.hasImage():
            pass
        # TODO 写完此函数


class ImageViewer(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.image: QImage = QImage()
        self.scale_factor: float = 1.0
        self.setWindowTitle("Image Viewer")
        self.resize(QGuiApplication.primaryScreen().availableSize() * 3 / 5)

        self.image_label = QLabel(self)
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_label.setScaledContents(True)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setBackgroundRole(QPalette.Dark)
        self.scroll_area.setWidget(self.image_label)
        self.scroll_area.setVisible(False)

        self.setCentralWidget(self.scroll_area)

        self.save_as_act = QAction()
        self.print_act = QAction()
        self.copy_act = QAction()
        self.zoom_in_act = QAction()
        self.zoom_out_act = QAction()
        self.normal_size_act = QAction()
        self.fit_to_window_act = QAction()
        self.create_actions()

    def load_file(self, file_name: str) -> bool:
        """
        打开文件，加载图片 \n
        :param file_name: 文件名
        :return: 是否成功加载文件
        """

        reader = QImageReader(file_name)
        reader.setAutoTransform(True)
        new_image = reader.read()
        if new_image.isNull():
            QMessageBox.information(
                self,
                QGuiApplication.applicationDisplayName(),
                f"Cannot load {QDir.toNativeSeparators(file_name)}: {reader.errorString()}",
            )
            return False

        self.set_image(new_image)

        self.setWindowFilePath(file_name)

        message = (
            f"Opened '{QDir.toNativeSeparators(file_name)}', "
            f"{self.image.width()}x{self.image.height()}, Depth: {self.image.depth()}"
        )
        self.statusBar().showMessage(message)
        return True

    def set_image(self, new_image: QImage) -> None:
        """
        将图像设置到滚动区域中，并展示 \n
        :param new_image: QImage图像
        :return: None
        """

        self.image = new_image
        if self.image.colorSpace().isValid():
            self.image.convertToColorSpace(QColorSpace.SRgb)
        self.image_label.setPixmap(QPixmap.fromImage(self.image))

        self.scale_factor = 1.0

        self.scroll_area.setVisible(True)
        self.print_act.setEnabled(True)
        self.fit_to_window_act.setEnabled(True)
        self.update_actions()

        if not self.fit_to_window_act.isChecked():
            self.image_label.adjustSize()

    def save_file(self, file_name: str) -> bool:
        writer = QImageWriter(file_name)

        if not writer.write(self.image):
            QMessageBox.information(
                self,
                QGuiApplication.applicationDisplayName(),
                f"Cannot write {QDir.toNativeSeparators(file_name)}: {writer.errorString()}",
            )
            return False
        message = f"Wrote '{QDir.toNativeSeparators(file_name)}'"
        self.statusBar().showMessage(message)
        return True

    def initialize_image_file_dialog(
        self, dialog: QFileDialog, accept_mode: QFileDialog.AcceptMode
    ) -> None:
        """
        配置文件对话框为只接受图像模式 \n
        :param dialog: 待配置的对话框
        :param accept_mode: 接受模式
        :return: None
        """

        first_dialog = True

        if first_dialog:
            first_dialog = False
            pictures_locations = QStandardPaths.standardLocations(QStandardPaths.PicturesLocation)
            if not pictures_locations:
                dialog_dir = QDir.currentPath()
            else:
                dialog_dir = pictures_locations[-1]
            dialog.setDirectory(dialog_dir)

        mime_type_filters: List[str] = []
        if accept_mode == QFileDialog.AcceptOpen:
            supported_mime_types = QImageReader.supportedMimeTypes()
        else:
            supported_mime_types = QImageWriter.supportedMimeTypes()

        for mime_type_name in supported_mime_types:
            mime_type_filters.append(str(mime_type_name))
        mime_type_filters.sort()

        dialog.setMimeTypeFilters(mime_type_filters)
        dialog.selectMimeTypeFilter("image/jpeg")
        dialog.setAcceptMode(accept_mode)
        if accept_mode == QFileDialog.AcceptSave:
            dialog.setDefaultSuffix("jpg")

    def open(self) -> None:
        dialog = QFileDialog(self, "Open File")
        self.initialize_image_file_dialog(dialog, QFileDialog.AcceptOpen)
        while dialog.exec() == QDialog.Accepted and not self.load_file(dialog.selectedFiles()[0]):
            ...

    def save_as(self) -> None:
        dialog = QFileDialog(self, "Save File As")
        self.initialize_image_file_dialog(dialog, QFileDialog.AcceptSave)

        while dialog.exec() == QDialog.Accepted and not self.save_file(dialog.selectedFiles()[0]):
            ...

    def print(self) -> None:
        pass

    def copy(self) -> None:
        QGuiApplication.clipboard().setImage(self.image)

    def paste(self) -> None:
        new_image = clipboard_image()

    def zoom_in(self) -> None:
        self.scale_image(1.25)

    def zoom_out(self) -> None:
        self.scale_image(0.8)

    def normal_size(self) -> None:
        self.image_label.adjustSize()
        self.scale_factor = 1.0

    def fit_to_window(self) -> None:
        fit_to_window_: bool = self.fit_to_window_act.isChecked()
        self.scroll_area.setWidgetResizable(fit_to_window_)
        if not fit_to_window_:
            self.normal_size()
        self.update_actions()

    def about(self) -> None:
        """
        展示本应用程序的关于信息 \n
        :return: None
        """

        QMessageBox.about(
            self,
            "About Image Viewer",
            "<p>The <b>Image Viewer</b> example shows how to combine QLabel "
            "and QScrollArea to display an image. QLabel is typically used "
            "for displaying a text, but it can also display an image. "
            "QScrollArea provides a scrolling view around another widget. "
            "If the child widget exceeds the size of the frame, QScrollArea "
            "automatically provides scroll bars. </p><p>The example "
            "demonstrates how QLabel's ability to scale its contents "
            "(QLabel::scaledContents), and QScrollArea's ability to "
            "automatically resize its contents "
            "(QScrollArea::widgetResizable), can be used to implement "
            "zooming and scaling features. </p><p>In addition the example "
            "shows how to use QPainter to print an image.</p>",
        )

    def create_actions(self) -> None:
        """
        创建菜单并添加actions \n
        :return: None
        """

        file_menu: QMenu = self.menuBar().addMenu("&File")

        open_act = file_menu.addAction("&Open...", self.open)
        open_act.setShortcut(QKeySequence.Open)

        # TODO 解决无法通过Mypy的问题
        save_as_act = file_menu.addAction("&Save As...", self.save_as)
        save_as_act.setEnabled(False)

        print_act = file_menu.addAction("&Print...", self.print)
        print_act.setShortcut(QKeySequence.Print)
        print_act.setEnabled(False)

        file_menu.addSeparator()

        exit_act = file_menu.addAction("E&xit", self.close)
        exit_act.setShortcut("Ctrl+Q")

        edit_menu = self.menuBar().addMenu("&Edit")

        self.copy_act = edit_menu.addAction("&Copy", self.copy)
        self.copy_act.setShortcut(QKeySequence.Copy)
        self.copy_act.setEnabled(False)

        paste_act: QAction = edit_menu.addAction("&Paste", self.paste)
        paste_act.setShortcut(QKeySequence.Paste)

        view_menu = self.menuBar().addMenu("&View")

        self.zoom_in_act = view_menu.addAction("Zoom &In (25%)", self.zoom_in)
        self.zoom_in_act.setShortcut(QKeySequence.ZoomIn)
        self.zoom_in_act.setEnabled(False)

        self.zoom_out_act = view_menu.addAction("Zoom &Out (25%)", self.zoom_out)
        self.zoom_out_act.setShortcut(QKeySequence.ZoomOut)
        self.zoom_out_act.setEnabled(False)

        self.normal_size_act = view_menu.addAction("&Normal Size", self.normal_size)
        self.normal_size_act.setShortcut("Ctrl+S")
        self.normal_size_act.setEnabled(False)

        view_menu.addSeparator()

        self.fit_to_window_act = view_menu.addAction("&Fit to Window", self.fit_to_window)
        self.fit_to_window_act.setEnabled(True)
        self.fit_to_window_act.setCheckable(True)
        self.fit_to_window_act.setShortcut("Ctrl+F")

        help_menu = self.menuBar().addMenu("&Help")

        help_menu.addAction("&About", self.about)
        help_menu.addAction("About &Qt", QApplication.aboutQt)

    def update_actions(self) -> None:
        """
        更新actions可用状态 \n
        :return: None
        """

        self.save_as_act.setEnabled(self.image.isNull())
        self.copy_act.setEnabled(self.image.isNull())
        self.zoom_in_act.setEnabled(not self.fit_to_window_act.isChecked())
        self.zoom_out_act.setEnabled(not self.fit_to_window_act.isChecked())
        self.normal_size_act.setEnabled(not self.fit_to_window_act.isChecked())

    def scale_image(self, factor: float) -> None:
        """
        缩放图像并调整相关控件 \n
        :param factor: 缩放比例系数
        :return: None
        """

        self.scale_factor *= factor
        self.image_label.resize(self.scale_factor * self.image_label.pixmap().size())
        self.adjust_scroll_bar(self.scroll_area.horizontalScrollBar(), factor)
        self.adjust_scroll_bar(self.scroll_area.verticalScrollBar(), factor)

        self.zoom_in_act.setEnabled(self.scale_factor < 3.0)
        self.zoom_out_act.setEnabled(self.scale_factor > 0.333)

    def adjust_scroll_bar(self, scroll_bar: QScrollBar, factor: float):
        """
        调整滚动条位置 \n
        :param scroll_bar: 滚动条实例
        :param factor: 缩放因数
        :return: None
        """

        scroll_bar.setValue(
            int(factor * scroll_bar.value() + ((factor - 1) * scroll_bar.pageStep() / 2))
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec())
