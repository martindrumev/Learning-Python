import sys
from PyQt5.QtWidgets import *



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()
        self.button = QPushButton("Clicked:")
        self.button.released.connect(self.clickedButton)
        self.button.pressed.connect(self.pressButton)


        h = QHBoxLayout()
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)

        self.setWindowTitle("Horizontal Layout")
        self.show()

    def clickedButton(self):
        print("This button has been released.")

    def pressButton(self):
        print("This button is being pressed.")
        self.counter += 1
        self.button.setText("Clicked: " + str(self.counter))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())