import sys
from PyQt5.QtWidgets import *



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("Hi there, I'm a label. Woot.")
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # QVBoxLayout give vertical layout
        horizontal = QHBoxLayout()
        horizontal.addStretch(1)

        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)

        vertical = QVBoxLayout()
        vertical.addWidget(label)
        vertical.addStretch(1)
        vertical.addLayout(horizontal)

        self.setLayout(vertical)

        self.setWindowTitle("Horizontal Layout")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())