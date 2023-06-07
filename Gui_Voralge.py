import sys, os
import time

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QRunnable, Slot, QThreadPool

from ui_MainWindow import Ui_MainWindow

class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__()
        self.args = args
        self.kwargs = kwargs

    @Slot()  # QtCore.Slot
    def work1(self):
        print("Thread 1 start")
        print(f"args: {self.kwargs['var1']}")

        MainWindow.ui.pushButton.setEnabled(False)
        time.sleep(5)
        MainWindow.ui.pushButton.setEnabled(True)

        print("Thread 1 complete")
    
    def work2(self):
        print("Thread 2 start")
        print(f"args: {self.kwargs['var2']}")

        MainWindow.ui.pushButton_2.setEnabled(False)
        time.sleep(2)
        MainWindow.ui.pushButton_2.setEnabled(True)

        print("Thread 2 complete")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(windowIcon)

        self.ui.pushButton.pressed.connect(self.aufgabe1)
        self.ui.pushButton_2.pressed.connect(self.aufgabe2)

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.show()

    def aufgabe1(self):
        worker = Worker(var1="var1")
        self.threadpool.start(worker.work1)

    def aufgabe2(self):
        worker = Worker(var2="var2")
        self.threadpool.start(worker.work2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowIcon = QIcon()
    windowIcon.addFile(os.path.abspath("data/icon.png"))

    MainWindow = MainWindow()

    app.exec()
