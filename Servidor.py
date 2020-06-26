from UI.ServerUI import Ui_ServerWindow
from PyQt5 import QtWidgets
from BK.ServidorBK import ServidorBk
import sys


class Servidor():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        ClientWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ServerWindow()
        self.ui.setupUi(ClientWindow)
        self.bk = ServidorBk(self.ui.txf_receive)
        self.actions()
        ClientWindow.show()
        sys.exit(app.exec_()) 

    def actions(self):
        self.ui.btn_starsv.clicked.connect(self.startServ)
        self.ui.btn_send.clicked.connect(self.enviarMsg)

    def startServ(self):
        self.bk.startConex(self.ui.btn_starsv)
    
    def enviarMsg(self):
        self.bk.sendToAllS(self.ui.txf_send)
    
    
if __name__ == "__main__":
    servidor = Servidor()