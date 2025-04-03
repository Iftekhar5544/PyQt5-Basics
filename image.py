import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.setGeometry(700, 350, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        label.setStyleSheet("background-color: rgb(255, 255, 255);")
 
        pixmap = QPixmap("nature.jpeg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        # Currently in center, you can make it to 9 position, practice later
        label.setGeometry((self.width() - label.width()) //2,
                          (self.height() - label.height()) //2,
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()