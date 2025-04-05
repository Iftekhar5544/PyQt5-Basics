# Step_01: Imports
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit

# Step_02: Create Main window and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(300, 400)

# Step_03: Add the app objects/widgets/GUI elements/ components

text_box = QLineEdit()

# We are using a loop to create the buttons so after creating a grid object we will have a loop to follow the steps
buttons = ["7", "8", "9", "+",
           "4", "5", "6", "-",
           "1", "2", "3", "*",
           "0", ".", "=", "/"]

clear = QPushButton("Clear")
delete = QPushButton("<")

# Step_05: Creating Function for button click
def button_clicked():
    button = app.sender()
    text = button.text()
    if text == "=":
        current_text = text_box.text()
        try:
            result = eval(current_text)
            text_box.setText(str(result))
        except Exception as e:
            text_box.setText(f"Error")
            print(f"Error: {e}")
    elif text == "Clear":
        text_box.clear()
    elif text == "<":
        current_text = text_box.text()
        text_box.setText(current_text[:-1])
    else:
        current_text = text_box.text()
        text_box.setText(current_text + text)

# Step_04: Add the design layout
# Steps:
#   1. Create master layout and sub layouts
#   2. Add "objects/widgets/GUI elements/ components" into those sub layouts
#   3. Add all the sub layouts into the master layout
#   4. Set master layout to the Main Window

# 1
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
grid = QGridLayout()
row2 = QHBoxLayout()

# 2
row1.addWidget(text_box)
row2.addWidget(clear)
row2.addWidget(delete)

# Steps_03, Step_04.2 & Step_6: <------ Steps to create buttons in a grid with for loop ------>
row = 0
col = 0
for text in buttons:
    button = QPushButton(text)
    grid.addWidget(button, row, col)
    button.clicked.connect(button_clicked)

    col += 1
    if col > 3:
        col = 0
        row += 1

# 3
master_layout.addLayout(row1)
master_layout.addLayout(grid)
master_layout.addLayout(row2)

# 4
main_window.setLayout(master_layout)



# Step_05: Functions that needed to operate/ control the application
# Note: In this app the function need to be added earlier for loop


# Step_06: Events handler which will call the functions as needed per task
clear.clicked.connect(button_clicked)
delete.clicked.connect(button_clicked)
# Note: I have my grib buttons already connected with the for loop

# Step_07: Show the main window and execute app
main_window.show()
app.exec_()
