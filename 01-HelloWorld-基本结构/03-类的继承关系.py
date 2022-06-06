from PySide6 import QtWidgets


def get_sub_classes(class_):
    """递归地显示某一类的所有子类"""
    for subclass in class_.__subclasses__():
        print(subclass)
        if len(class_.__subclasses__()) > 0:
            get_sub_classes(subclass)


# 查看QAbstractButton抽象基类的所有子类，了解Qt6提供了哪些按钮控件
get_sub_classes(QtWidgets.QAbstractButton)
