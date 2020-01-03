import pika
import threading
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel2 = connection.channel()
channel2.queue_declare(queue='colaClientes')

channel3 = connection.channel()
channel3.queue_declare(queue='colaOpciones')

nombre = input("Cual es tu nombre?")
channel = connection.channel()
channel.queue_declare(queue=nombre)

channel2.basic_publish(exchange='', routing_key='colaClientes', body=nombre)

def recibeMensaje(ch, method, properties, body):
    print("Mensaje recibido: " + str(body,'utf-8'))

#def recibir(nombre):
#    channel.basic_consume(queue=nombre, on_message_callback=recibeMensaje, auto_ack=True)
    
#t = threading.Thread(target=recibir, args=nombre)
#t.start()

while True:

    print("Seleccione una opcion:")
    print("1. Enviar mensaje.")
    print("2. Recibir mensaje.")
    print("3. Ver mensajes enviados.")
    print("4. Ver listado de clientes.")
    print("5. Cerrar cliente.")
    print("6. Cerrar servidor.")
    op = input()

    channel.basic_publish(exchange='', routing_key='colaOpciones', body=op)
    
    if(op == '1'):
        receptor = input("A quien quiere enviar el mensaje?")
        msg = input("Ingrese un mensaje: ")
        channel.basic_publish(exchange='', routing_key=receptor, body=msg)
        dateTimeObj = datetime.now()
        timestamp = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
        print("[{}] envia a [{}] el mensaje: {} [{}]".format(nombre, receptor, msg, timestamp))

    elif(op == '2'):
        channel.basic_consume(queue=nombre, on_message_callback=recibeMensaje, auto_ack=True)
        channel.start_consuming()
        channel.stop_consuming()

    #elif(op == '3'):
    #    def recibeCliente(ch, method, properties, body):
    #        cli = str(body,'utf-8')
    #        clientes.append(cli)
    #        print(clientes)
    #    channel.basic_consume(queue='colaClientes', on_message_callback=recibeCliente, auto_ack=True)

    elif(op == '4'):
        print("Cerrando cliente...")
        break

    elif(op == '5'):
        print("Cerrando servidor...")
        break

    else:
        print("Opcion invalida, ingrese nuevamente.")

connection.close()