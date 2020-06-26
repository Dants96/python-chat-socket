# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\ClientWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ClientWindow(object):
    def setupUi(self, ClientWindow):
        ClientWindow.setObjectName("ClientWindow")
        ClientWindow.resize(380, 370)
        ClientWindow.setIconSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(ClientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.txf_send = QtWidgets.QLineEdit(self.centralwidget)
        self.txf_send.setObjectName("txf_send")
        self.gridLayout.addWidget(self.txf_send, 2, 1, 1, 1)
        self.txf_receive = QtWidgets.QTextEdit(self.centralwidget)
        self.txf_receive.setReadOnly(True)
        self.txf_receive.setObjectName("txf_receive")
        self.gridLayout.addWidget(self.txf_receive, 1, 1, 1, 1)
        self.btn_receive = QtWidgets.QPushButton(self.centralwidget)
        self.btn_receive.setObjectName("btn_receive")
        self.gridLayout.addWidget(self.btn_receive, 1, 2, 1, 1)
        self.btn_conect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_conect.setObjectName("btn_conect")
        self.gridLayout.addWidget(self.btn_conect, 0, 1, 1, 1)
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setObjectName("btn_send")
        self.gridLayout.addWidget(self.btn_send, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        ClientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClientWindow)
        self.statusbar.setObjectName("statusbar")
        ClientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClientWindow)
        QtCore.QMetaObject.connectSlotsByName(ClientWindow)

    def retranslateUi(self, ClientWindow):
        _translate = QtCore.QCoreApplication.translate
        ClientWindow.setWindowTitle(_translate("ClientWindow", "Cliente"))
        self.btn_receive.setText(_translate("ClientWindow", "Receive"))
        self.btn_conect.setText(_translate("ClientWindow", "Conect"))
        self.btn_send.setText(_translate("ClientWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClientWindow = QtWidgets.QMainWindow()
    ui = Ui_ClientWindow()
    ui.setupUi(ClientWindow)
    ClientWindow.show()
    sys.exit(app.exec_())
