# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PieChart import PieChart


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qmlRegisterType(PieChart, 'Charts', 1, 0, 'PieChart')
    engine.load(os.path.join(os.path.dirname(__file__), "app.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
