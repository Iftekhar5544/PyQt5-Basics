# Step_01: Imports
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
)
from PyQt5.QtGui import QIcon

# Step_02: Create Main window and settings
app = QApplication([])
main_window = QWidget()
#main_window.setWindowIcon(QIcon("images/icon.png")) uncomment and set path for app icon
main_window.setWindowTitle("Calculator")
main_window.resize(500, 700)

# Step_03: Add the app objects/widgets/GUI elements/components
# Example:
# button1 = QPushButton("1")
# display = QLineEdit()

# Step_04: Add the design layout
# Steps:
#   1. Create master layout and sub layouts
#       e.g. main_layout = QVBoxLayout()
#            button_layout = QGridLayout()
#   2. Add "objects/widgets/GUI elements/ components" aka widgets into those sub layouts
#       e.g. button_layout.addWidget(button1, 0, 0)
#   3. Add all the sub layouts into the master layout
#       e.g. main_layout.addLayout(button_layout)
#   4. Set master layout to the Main Window
#       e.g. main_window.setLayout(main_layout)

# Step_05: Functions needed to operate/control the application
# e.g. def calculate_result(): ...

# Step_06: Events handler which will call the functions as needed per task
# e.g. button1.clicked.connect(calculate_result)

# Step_07: Show the main window and execute app
main_window.show()
app.exec_()
