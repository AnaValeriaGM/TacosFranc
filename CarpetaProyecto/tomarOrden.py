import boto3


def tomarOrden():
	sqs = boto3.client('sqs')

	response = sqs.receive_message(
    	QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4'
	)

	recibos = []
	ordenes= []

	for message in response["Messages"]:
		recibos.append(message["ReceiptHandle"])
		ordenes.append(message["Body"])
	return ordenes

def escribirJson(ordenes):
	archivo=open("ordenesJSON","a")
	for i in ordenes:
		archivo.write(i + "\n")
		print(i)
	archivo.close()

escribirJson(tomarOrden())

#for r in recibos:
   # response = sqs.delete_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4',ReceiptHandle=r)
