# Imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

# Main App objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Generator")
main_window.resize(400, 200)

# Create all app objects
title = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")

# All Design here
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

#
row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

#
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Create Functions for your task/works
my_words = ["apple", "banana", "orange", "grape", "watermelon", "kiwi", "mango", "strawberry", "blueberry", "raspberry", "pineapple", "peach", "plum", "lemon", "lime"]
def rand_word1():
    word = choice(my_words)
    text1.setText(word)

def rand_word2():
    word = choice(my_words)
    text2.setText(word)

def rand_word3():
    word = choice(my_words)
    text3.setText(word)

# Events

button1.clicked.connect(rand_word1)
button2.clicked.connect(rand_word2)
button3.clicked.connect(rand_word3)

# Show/ Run the app
main_window.show()
app.exec_()