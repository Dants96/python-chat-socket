import socket, threading, sys, pickle
import UI.AlertsHTML as out

class ClienteBk():
    def __init__(self, tx_recv):
        self.host = "localhost"
        self.port = 7000
        self.tx_recv = tx_recv

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
                    data = pickle.loads(data)
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
     