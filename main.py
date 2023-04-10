import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(('123','3123','312'))
        self.setWindowTitle('I love pancakes')
        self.text = QtWidgets.QLabel('Hello Vlad')
        self.button = QtWidgets.QPushButton('do not push me')
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text,
                              alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.combo)
        self.button.clicked.connect(self.click)

    def click(self):
        self.text.setText('I have asked')


if __name__ == '__main__':
    application = QtWidgets.QApplication()
    widget = Window()
    widget.resize(300, 200)
    widget.show()

    sys.exit(application.exec())
