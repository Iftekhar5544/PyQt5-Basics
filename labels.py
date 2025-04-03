import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.setGeometry(700, 350, 500, 400)
        self.setWindowIcon(QIcon("icon.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0, 500, 300)
        label.setStyleSheet("color: #383838;"
                            "background-color: #98fae0;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop) # Vertically Top (Top Left)
        #label.setAlignment(Qt.AlignVCenter)  # Vertically Center (Left Mid)
        #label.setAlignment(Qt.AlignBottom) # Vertically Bottom

        #label.setAlignment(Qt.AlignRight) #Horizontally Right (Right Top)
        #label.setAlignment(Qt.AlignRight | Qt.AlignVCenter) # Right Center
        #label.setAlignment(Qt.AlignRight | Qt.AlignBottom)  # Right Bottom

        #label.setAlignment(Qt.AlignHCenter)  # Horizontally Center (Top Mid)
        #label.setAlignment(Qt.AlignLeft)  # Horizontally Left (Top Left)

        #label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter) # Center & Bottom

        label.setAlignment(Qt.AlignCenter) # Center & Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()