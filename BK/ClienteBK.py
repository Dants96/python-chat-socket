import socket, threading, sys, pickle
import UI.AlertsHTML as out

class ClienteBk():
    def __init__(self, tx_recv, tx_field):
        self.host = "localhost"
        self.port = 7000
        self.tx_recv = tx_recv
        self.tx_field = tx_field

    def conectar(self, btn):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((str(self.host), int(self.port)))
            self.tx_recv.append(out.alertSucces("Conectado al servidor"))
            msg_recv = threading.Thread(target=self.msg_recv)
            msg_recv.daemon = True
            msg_recv.start()
            btn.setEnabled(False)
        except:
            print("Error Servidor desconectado")
            self.tx_recv.append(out.alertFail("Error servidor desconectado"))


    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    data = str(pickle.loads(data))
                    if len(data) >= 8 and data[0:8] == "RQSuccs!":
                        # nombre encontrado 
                        self.tx_field.setText("{}".format(data[8:len(data)]))
                        self.tx_recv.append("Servidor -> {}".format(out.alertInfo("Nombre encontrado!")))
                    elif len(data) >= 8 and data[0:8] == "RQError!":
                        # hubo un error
                        self.tx_recv.append("Servidor -> {}".format(out.alertFail2(data[8:len(data)])))
                    else:
                        print(data)
                        self.tx_recv.append(data)
            except:
                pass

    def send_msg(self, field):
        msg = field.text()
        try:
            self.sock.send(pickle.dumps(msg))
            self.tx_recv.append("Cliente [YO]: {}".format(msg))
            field.setText("")
        except:
            print("Error Servidor desconectado")
            self.tx_recv.append(out.alertFail("Error servidor desconectado"))
    
    def send_reqDB(self, field):
        req = "Req_DB{}".format(field.text()) 
        try:
            self.sock.send(pickle.dumps(req))
            self.tx_recv.append(out.alertInfo("Peticion a base de datos enviada"))
        except:
            print("Error servidor desconectado")
            self.tx_recv.append(out.alertFail("Error servidor desconectado"))
                    