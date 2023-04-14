from PySide6.QtGui import QColor
from PySide6 import QtWidgets

colors = [("Red", "#FF0000"),
          ("Green", "#00FF00"),
          ("Blue", "#0000FF"),
          ("Black", "#000000"),
          ("White", "#FFFFFF"),
          ("Electric Green", "#41CD52"),
          ("Dark Blue", "#222840"),
          ("Yellow", "#F9E56d")]


def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i + 2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])


class Table(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        self.setColumnCount(len(colors[0]) + 1)
        self.setRowCount(len(colors))
        self.setHorizontalHeaderLabels(('name', 'code', 'color'))

        for i, (name, code) in enumerate(colors):
            tab_name = QtWidgets.QTableWidgetItem(name)
            tab_code = QtWidgets.QTableWidgetItem(code)
            tab_color = QtWidgets.QTableWidgetItem()
            tab_color.setBackground(get_rgb_from_hex(code))
            self.setItem(i, 0, tab_name)
            self.setItem(i, 1, tab_code)
            self.setItem(i, 2, tab_color)


if __name__ == '__main__':
    app=QtWidgets.QApplication()
    table = Table()
    table.show()
    app.exec()
