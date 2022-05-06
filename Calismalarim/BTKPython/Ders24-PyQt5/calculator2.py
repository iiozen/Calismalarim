from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_UI_MainWindow
class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_UI_MainWindow()
        self.ui.setupUi(self)


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()
