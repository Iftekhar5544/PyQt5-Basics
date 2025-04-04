# Step_01: Imports
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont, QIcon

# Step_02: Create Main window class inside this class define settings and ui
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.resize(400, 600)
        self.setWindowIcon(QIcon("CalcIcon.png"))
        # Call the initUI function
        self.initUI()

    # Define the App Interface with initUI which will be called by __init__()
    def initUI(self):

        # Step_03: Add the app objects/widgets/GUI elements/ components
        self.text_box = QLineEdit()
        #self.text_box.setFont(QFont("Helvetica", 32))
        self.text_box.setReadOnly(True)


        # We are using a loop to create the buttons, so after creating a grid object we will have a loop to follow the steps
        buttons = ["7", "8", "9", "+",
                   "4", "5", "6", "-",
                   "1", "2", "3", "*",
                   "0", ".", "=", "/"]

        clear = QPushButton("Clear")
        delete = QPushButton("<")
        #clear.setStyleSheet("QPushButton { font-family: 'Comic Sans MS'; font-size: 25pt; padding: 10px; }")
        #delete.setStyleSheet("QPushButton { font-family: 'Comic Sans MS'; font-size: 25pt; padding: 10px; }")

        # Step_04: Add the design layout
        # Steps:
        #   1. Create master layout and sub layouts
        #   2. Add "objects/widgets/GUI elements/ components" aka widgets into those sub layouts
        #   3. Add all the sub layouts into the master layout
        #   4. Set master layout to the Main Window

        # 1
        master_layout = QVBoxLayout()
        row1 = QHBoxLayout()
        grid = QGridLayout()
        row2 = QHBoxLayout()

        # 2
        row1.addWidget(self.text_box)
        row2.addWidget(clear)
        row2.addWidget(delete)

        # Steps_03, Step_04.2 & Step_5: <------ Steps to create buttons in a grid with for loop ------>
        row = 0
        col = 0
        for text in buttons:
            button = QPushButton(text)

            grid.addWidget(button, row, col)
            button.clicked.connect(self.button_clicked)
            #button.setStyleSheet("QPushButton { font-family: 'Comic Sans MS'; font-size: 25pt; padding: 10px; }")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # 3
        master_layout.addLayout(row1)
        master_layout.addLayout(grid)
        master_layout.addLayout(row2)
        master_layout.setContentsMargins(25,25,25,25)

        # 4
        self.setLayout(master_layout)

        # Step_05: Events handler which will call the functions as needed per task
        clear.clicked.connect(self.button_clicked)
        delete.clicked.connect(self.button_clicked)
        # Note: I have my grid buttons already connected with the for loop

    # Step_06: Creating Function for button click
    def button_clicked(self):
        button = app.sender()
        text = button.text()
        if text == "=":
            current_text = self.text_box.text()
            try:
                result = eval(current_text)
                self.text_box.setText(str(result))
            except Exception as e:
                self.text_box.setText(f"Error")
                print(f"Error: {e}")
        elif text == "Clear":
            self.text_box.clear()
        elif text == "<":
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])
        else:
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text)


# Step_07: Create app and main window object
app = QApplication([])
# Step_08: Set global styles for the app
app.setStyleSheet("""
    QWidget {
        background-color: #e8e8e1;
    }

    QLineEdit {
        font-family: 'Comic Sans MS';
        color: #03051f;
        font-size: 32pt;
        padding: 10px;
        background-color: #f5f5f5;
        border: 2px solid #ccc;
        border-radius: 8px;
    }

    QPushButton {
        font-family: 'Comic Sans MS';
        color: #03051f;
        font-size: 25pt;
        padding: 10px;
        border: None;
        background-color: #f5f5f5;
        border-radius: 10px;
    }

    QPushButton:hover {
        background-color: #dcdcdd;
    }
""")

main_window = MainWindow()
#main_window.setStyleSheet("QWidget {background-color: #e8e8e1}")
# Step_09: Show the main window and execute app
main_window.show()
app.exec_()
