#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bajarResolucion
from socket import socket

def main():
    s = socket()
    s.connect(("172.24.88.101", 6030))

    while True:
        f = open("compress_a2.jpg", "rb")
        content = f.read(1024)

        while content:
            # Enviar contenido.
            s.send(content)
            content = f.read(1024)
        break

    # Se utiliza el caracter de codigo 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        s.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))

    # Cerrar conexion y archivo.
    s.close()
    f.close()
    print("El archivo ha sido enviado correctamente.")


if __name__ == "__main__":
    print("inicia el cliente")
    bajarResolucion.bajarResolucion()
    print("Se baja la resolucion primero")
    main()
    print("Ya se envio la foto de verdad")


