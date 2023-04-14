from PySide6 import QtWidgets


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle('Form')
        self.text_edit = QtWidgets.QLineEdit('Write your name here')
        self.button = QtWidgets.QPushButton('See greetings')

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.greeting)
        self.text = QtWidgets.QLabel()
        self.clicked = False

    def greeting(self):
        if not self.clicked:
            self.layout.addWidget(self.text)
            self.clicked = True
        self.text.setText(f'Hello {self.text_edit.text()}')


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window=QtWidgets.QMainWindow()
    dialog = Form(window)
    window.show()
    dialog.show()
    app.exec()
