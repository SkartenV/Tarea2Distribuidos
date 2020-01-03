from concurrent import futures

import grpc
import time
import os

import proto.ChatRPC_pb2 as chat
import proto.ChatRPC_pb2_grpc as rpc


class ChatServidor(rpc.ChatServidorServicer):

    def __init__(self):
        self.chats = []
        self.clientes = []
        self.diccionario = dict()

    def ChatStream(self, request_iterator, context):

        lastindex = 0
        while True:
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n

    def EnviarMensaje(self, request: chat.Mensaje, context):

        if(request.Receptor == "servidor"):
            self.diccionario[request.Nombre] = []
            self.clientes.append(request.Nombre)
            print(self.clientes)
            return chat.Vacio()
        elif(request.Receptor == "salir"):
            file.close()
            os._exit(0)

        self.diccionario[request.Nombre].append(request.Texto)
        StringMensaje = "[{}] envia a [{}] el mensaje: {} [{}]".format(request.Nombre, request.Receptor, request.Texto, request.Tiempo)
        
        file.write(StringMensaje + os.linesep)
        
        self.chats.append(request)
        return chat.Vacio()

    def HistorialChat(self, request: chat.Mensaje, context):
        x = chat.Mensaje()
        x.Receptor = request.Nombre
        x.Nombre = "historial"
        delimeter = ','
        Historial = delimeter.join(self.diccionario[request.Nombre])
        x.Texto = Historial
        self.chats.append(x)
        return chat.Vacio()
        
    def ListaClientes(self, request: chat.Mensaje, context):
        x = chat.Mensaje()
        x.Receptor = request.Nombre
        x.Nombre = "clientes"
        delimeter = ','
        listaClientes = delimeter.join(self.clientes)
        x.Texto = listaClientes
        self.chats.append(x)
        return chat.Vacio()

if __name__ == '__main__':
    port = 11912
    file = open("./log.txt", "w")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_ChatServidorServicer_to_server(ChatServidor(), server)
    print('Servidor activo. Esperando conexiones...')
    server.add_insecure_port('[::]:' + str(port))
    server.start()

    while True:
        time.sleep(64 * 64 * 100) 