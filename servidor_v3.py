__author__ = 'KeylorG'

import socket
from threading import Thread
import datetime
import re
from subprocess import Popen, PIPE, check_output

class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)

        self.conn = conn
        self.addr = addr
        self.clients = []

    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024).decode('utf-8')
                self.clients.append(input_data)
            except socket.error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    #print(input_data)
                    if input_data == "nombre":
                        nombre= socket.gethostname()
                        nombre= "El nombre del host corresponde a: "+nombre
                        self.conn.send(nombre.encode('utf-8'))
                        input_data=""
                    if input_data == "IP":
                        nombre2=socket.gethostname()
                        ipservidor= socket.gethostbyname(nombre2)
                        ipservidor="El IP del computador corresponde a: "+ipservidor
                        self.conn.send(ipservidor.encode('utf-8'))
                        input_data=""
                    if input_data == "task":
                        task= self.get_processes_running()
                        int(task)
                        task="La cantidad de procesos en ejecucion corresponde a: "+str(task)
                        self.conn.send(task.encode('utf-8'))
                        input_data=""
                    if input_data.find('/') > 0:
                        pais = pytz.timezone(input_data)
                        ahora = datetime.datetime.now(pais)
                        otra = str(ahora)
                        otra="La hora del pais seleccionado corresponde a: "+otra
                        self.conn.send(otra.encode('utf-8'))
                        input_data=""
                    else:
                        self.conn.send(input_data.encode('utf-8'))


    def get_processes_running(self):
        """
        Takes tasklist output and parses the table into a dict
        """
        tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
        p = []
        for task in tasks:
            m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())

            if m is not None:
                p.append({"image": m.group(1).decode()})
        contador = len(p)
        contador = str(contador)
        return (contador)

def main():
    s = socket.socket()
    # Escuchar peticiones en el puerto 6030.
    s.bind(("172.24.99.91", 6030))
    s.listen(0)

    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado." % addr)
if __name__ == "__main__":
    main()