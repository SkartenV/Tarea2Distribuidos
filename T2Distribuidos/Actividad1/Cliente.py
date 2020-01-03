import threading
from tkinter import *
from tkinter import simpledialog

import grpc
from datetime import datetime

import proto.ChatRPC_pb2 as chat
import proto.ChatRPC_pb2_grpc as rpc

address = 'localhost'
port = 11912


class Cliente:

    def __init__(self, u: str):

        self.username = u
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.conn = rpc.ChatServidorStub(channel)
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

        m = chat.Mensaje()
        m.Receptor = "servidor"
        m.Nombre = self.username
        m.Texto = "texto"
        self.conn.EnviarMensaje(m)
        while True:
            print("Seleccione una opcion:")
            print("1. Enviar mensaje.")
            print("2. Ver mensajes enviados")
            print("3. Ver listado de clientes")
            print("4. Cerrar cliente.")
            print("5. Cerrar servidor.")
            op = input()
            if(op == '1'):
                self.send_message(0)
            elif(op == '2'):
                x = chat.Mensaje()
                x.Receptor = "receptor"
                x.Nombre = self.username
                x.Texto = "texto"
                self.conn.HistorialChat(x)
            elif(op == '3'):
                x = chat.Mensaje()
                x.Receptor = "receptor"
                x.Nombre = self.username
                x.Texto = "texto"
                self.conn.ListaClientes(x)
            elif(op == '4'):
                break
            elif(op == '5'):
                x = chat.Mensaje()
                x.Receptor = "salir"
                x.Nombre = self.username
                x.Texto = "texto"
                self.conn.EnviarMensaje(x)
            else:
                print("Opcion invalida, ingrese nuevamente.")
            
    def __listen_for_messages(self):

        for mensaje in self.conn.ChatStream(chat.Vacio()):
            if(self.username == mensaje.Receptor):
                if(mensaje.Nombre == "historial"):
                    print("Estos son los mensajes que has enviado: {}".format(mensaje.Texto))
                elif(mensaje.Nombre == "clientes"):
                    print("Listado de clientes: {}".format(mensaje.Texto))
                else:
                    print("[{}] recibe desde [{}] el mensaje: {} [{}]".format(mensaje.Receptor, mensaje.Nombre, mensaje.Texto, mensaje.Tiempo))

    def send_message(self, event):

        n = chat.Mensaje()

        recep = input("A quien quiere enviar el mensaje?")
        if recep is not '':
            n.Receptor = recep

        message = input("Ingrese un mensaje: ")
        if message is not '':
            n.Nombre = self.username
            n.Texto = message
            dateTimeObj = datetime.now()
            timestamp = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
            n.Tiempo = timestamp
            print("[{}] envia a [{}] el mensaje: {} [{}]".format(n.Nombre, n.Receptor, n.Texto, n.Tiempo))
            self.conn.EnviarMensaje(n)

if __name__ == '__main__':
    username = None
    while username is None:
        username = input("Cual es tu nombre?")
    c = Cliente(username)