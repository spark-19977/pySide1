import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('active')
        self.button=QPushButton('click me')
        self.button.clicked.connect(self.click)
        self.setCentralWidget(self.button)

    def click(self):
        self.button.setText('you already cleacked it')
        self.button.setDisabled(True)
        self.setWindowTitle('nonactive')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()