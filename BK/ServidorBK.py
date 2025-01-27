import socket, pickle, threading, sys
import UI.AlertsHTML as out
from BK.BasedeDatos import BasedeDatos as db

class ServidorBk():
    def __init__(self, tx_recv):
        # guardar clientes conectados 
        self.clientes = []
        self.host = "192.168.0.20"
        self.port = 7000
        self.tx_recv = tx_recv

    def startConex(self, btn):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((str(self.host), int(self.port)))
            self.sock.listen(10)
            self.sock.setblocking(False)
            self.tx_recv.append(out.alertSucces("Servidor en linea"))
            aceptar = threading.Thread(target=self.aceptarCon)
            procesar = threading.Thread(target=self.procesarCon)
            aceptar.daemon = True
            aceptar.start()
            procesar.daemon = True
            procesar.start()
            
            btn.setEnabled(False)
        except:
            self.tx_recv.append(out.alertFail("Error al iniciar servidor"))

            
    def msgToAll(self, msg, cliente_src):
            for cliente in self.clientes:
                try:
                    if cliente != cliente_src:
                        cliente.send(msg)
                except:
                    print("Cliente desconectado, conexion eliminada")
                    self.tx_recv.append(out.alertInfo("Cliente desconectado, conexion eliminada"))
                    self.clientes.remove(cliente)
            self.tx_recv.append(pickle.loads(msg))
            
    def sendToAllS(self, field):
        msg = field.text()
        for cliente in self.clientes:
            try:
                cliente.send(pickle.dumps(out.alertInfo("Servidor -> {}".format(msg))))
                field.setText("")
            except:
                print("Cliente desconectado {}, conexion eliminada".format((self.clientes.index(cliente) + 1)))
                self.tx_recv.append(out.alertInfo("Cliente desconectado {}, conexion eliminada".format((self.clientes.index(cliente) + 1))))
                self.clientes.remove(cliente)
        self.tx_recv.append("Servidor -> {}".format(msg))
      
    
            
    def aceptarCon(self):
        print("Aceptando conexiones...")
        self.tx_recv.append(out.alertInfo("Aceptando Conexiones..."))
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
                self.tx_recv.append("Cliente agregado no {}".format(len(self.clientes)))
            except:
                pass

    def procesarCon(self):
        print("Procesando conexiones ...")
        self.tx_recv.append(out.alertInfo("Aceptando peticiones..."))
        while True:
            if len(self.clientes) > 0:
                for cliente in self.clientes:
                    try:
                        data = cliente.recv(1024)
                        if data:
                            data = str(pickle.loads(data))
                            if data[0:6] == "Req_DB":
                                self.tx_recv.append(out.alertInfo("petion a base dedatos Cliente[{}]".format((self.clientes.index(cliente) + 1))))
                                busqueda = db.reqName(data[6:len(data)])
                                if busqueda["get"]:
                                    cliente.send(pickle.dumps("RQSuccs!{}".format(busqueda["req"])))
                                else:
                                    cliente.send(pickle.dumps("RQError!{}".format(busqueda["req"])))
                            else:
                                msg_u = "Cliente [{}]: {}".format((self.clientes.index(cliente) + 1), data)
                                data = pickle.dumps(msg_u)
                                self.msgToAll(data, cliente)
                    except:
                        pass
    
    def buscarEnBD(self, field, tx_recv_us):
        pass