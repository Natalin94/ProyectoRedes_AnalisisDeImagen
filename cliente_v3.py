_author_ = 'Natalin'
from socket import socket
# Compatibilidad con Python 3
try:
    raw_input
except NameError:
    raw_input = input
__author__ = 'Natalin'
from socket import socket
# Compatibilidad con Python 3
try:
    raw_input
except NameError:
    raw_input = input
def main():
    s = socket()
    s.connect(("172.24.163.80", 6030))

    while True:
        output_data = raw_input("> ")

        if output_data:
            # Enviar entrada. Comptabilidad con Python 3.
            try:
                s.send(output_data)
            except TypeError:
                s.send(bytes(output_data, "utf-8"))

            # Recibir respuesta.
            input_data = s.recv(1024)
            if input_data:
                # En Python 3 recv() retorna los datos leídos
                # como un vector de bytes. Convertir a una cadena
                # en caso de ser necesario.
                print(input_data.decode("utf-8") if
                      isinstance(input_data, bytes) else input_data)

if __name__ == "__main__":
    main()