from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtGui, QtWidgets, QtCore

import sys
import ctypes

import queue


class RLMMSDKGUI(ApplicationContext):
    """The main window"""
    def __init__(self):
        super().__init__()

        #f = open(self.get_resource("style.css"))
        #style = f.read()
        #f.close()

        self.window = QtWidgets.QMainWindow()

        width = 1000
        height = 500
        #xpos = int((self.primaryScreen().size().width()-width)/2)
        #ypos = int((self.primaryScreen().size().height()-height)/2)

        self.window.setGeometry(0, 0, width, height)
        self.window.show()

if __name__ == '__main__':
    appctxt = ApplicationContext()
    app = RLMMSDKGUI()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(_version.__appid__)
