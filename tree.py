from PySide6 import QtWidgets

data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": []}


class Tree(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(Tree, self).__init__(parent)
        self.setColumnCount(2)
        self.setHeaderLabels(('name', 'type'))
        items = []
        for key, values in data.items():
            item = QtWidgets.QTreeWidgetItem((key,))
            for file in values:
                extension = file.split('.')[-1]
                row = QtWidgets.QTreeWidgetItem((file, extension))
                item.addChild(row)
            items.append(item)
        self.insertTopLevelItems(0, items)


if __name__ == '__main__':
    app=QtWidgets.QApplication()
    window = Tree()
    window.show()
    app.exec()


