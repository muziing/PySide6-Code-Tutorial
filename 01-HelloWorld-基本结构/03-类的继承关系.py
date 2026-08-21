from PySide6 import QtWidgets

# PySide6 现在懒加载，**类不被访问，就不会出现在`__subclasses__()`**。
# `__subclasses__()` 做 Qt 继承树遍历这个写法，现在已经不太靠谱，属于旧教程遗留
# 强制引用几个子类，触发加载到内存
_ = QtWidgets.QPushButton
_ = QtWidgets.QRadioButton
_ = QtWidgets.QCheckBox
_ = QtWidgets.QToolButton


def get_sub_classes(class_):
    for subclass in class_.__subclasses__():
        print(subclass)
        get_sub_classes(subclass)


app = QtWidgets.QApplication([])
get_sub_classes(QtWidgets.QAbstractButton)
