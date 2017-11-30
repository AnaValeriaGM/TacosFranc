
import boto3
import json

def escribirJSON():
    archivo = open("ordenes.json", 'a')
    sqs = boto3.client('sqs')
    respuesta = sqs.receive_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4",
        MaxNumberOfMessages = 5)
    
    if respuesta == None:
        return
    
    for orden in respuesta["Messages"]:
        archivo.write(orden["Body"] + "\n")
        print(orde)
    archivo.close()

def leerSQS():
    listaOrdenes = []
    sqs = boto3.client('sqs')
    respuesta = sqs.receive_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4"
        MaxNumberOfMessages = 5)
    if respuesta == None:
        return
    else:
        for orden in respuesta["Messages"]:
            listaOrdenes.append(json.loads(orden["Body"]))
            for r in recibos:
                response = sqs.delete_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4',ReceiptHandle=r
    return listaOrdenes

def escribirSQS(message):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName="cc406_response4")
    print(queue.url)
    respuesta = queue.send_message(MessageBody=message)
