#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import socket, error
import determinaMedidas
def main():
    print("Se inicia el servidor")
    s = socket()
    nombreImagen="recibida.jpg"

    # Escuchar peticiones en el puerto 6030.
    s.bind(("172.24.107.154", 6030))
    s.listen(0)

    conn, addr = s.accept()
    f = open("recibida.jpg", "wb")
    print("Se recibe la imagen del servidor")
    print("Se va a determinar medidas con el nombre de la imagen a analizar", nombreImagen)

    cont =0
    while (cont<5000):
        try:
            # Recibir datos del cliente.
            input_data = conn.recv(1024)
            cont += 1
           # print(cont)
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                    cont += 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                    cont+=1
                if end:
                    break
    determinaMedidas.recibeInformacionImagen()
    print("El archivo se ha recibido correctamente. Y termina el analisis")
    f.close()



if __name__ == "__main__":
    main()