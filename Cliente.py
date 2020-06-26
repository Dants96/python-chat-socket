from UI.ClienteUI import Ui_ClientWindow
from PyQt5 import QtWidgets
from BK.ClienteBK import ClienteBk
import sys

class Cliente:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        ClientWindow = QtWidgets.QMainWindow()
        
        self.ui = Ui_ClientWindow()
        self.ui.setupUi(ClientWindow)
        self.bk = ClienteBk(self.ui.txf_receive) 
        self.actions()
        
        ClientWindow.show()
        sys.exit(app.exec_())
        

    def actions(self):
        self.ui.btn_conect.clicked.connect(self.conectar)
        self.ui.btn_send.clicked.connect(self.enviarMsg)
        
    def enviarMsg(self):
        self.bk.send_msg(self.ui.txf_send)
    
    def conectar(self):
        self.bk.conectar(self.ui.btn_conect)


if __name__ == "__main__":
    cliente = Cliente()