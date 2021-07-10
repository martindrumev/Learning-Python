#!/usr/bin/python3

import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile("man.qml"))

    sys.exit(app.exec_())