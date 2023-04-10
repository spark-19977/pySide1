import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton

app = QApplication(sys.argv)

window = QMainWindow()

button=QPushButton('click')
window.setCentralWidget(button)
window.show()

# Start the event loop.
app.exec()