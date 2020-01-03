import pika
import os

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='colaMensajes')

channel2 = connection.channel()
channel2.queue_declare(queue='colaClientes')

channel3 = connection.channel()
channel3.queue_declare(queue='colaOpciones')

clientes = []

def recibeCliente(ch, method, properties, body):
    cli = str(body,'utf-8')
    clientes.append(cli)
    print(clientes)

def recibeMensaje(ch, method, properties, body):
    print("Mensaje recibido: " + str(body,'utf-8'))

def recibeOpcion(ch, method, properties, body):
    opcion = str(body,'utf-8')
    if(opcion == '1'):
        channel.basic_consume(queue='colaMensajes', on_message_callback=recibeMensaje, auto_ack=True)
    #elif(opcion == '2'):

    #elif(opcion == '3'):
        #channel.basic_publish(exchange='', routing_key='colaClientes', body="clientes")

    #elif(opcion == '4'):

    elif(opcion == '5'):
        os._exit(0)

channel.basic_consume(queue='colaClientes', on_message_callback=recibeCliente, auto_ack=True)

channel.basic_consume(queue='colaOpciones', on_message_callback=recibeOpcion, auto_ack=True)

channel.start_consuming()