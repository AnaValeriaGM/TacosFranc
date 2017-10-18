import boto3

sqs = boto3.client('sqs')

response = sqs.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4'
)

recibos = []

for message in response["Messages"]:
    recibos.append(message["ReceiptHandle"])
    print(message["Body"])

#for r in recibos:
   # response = sqs.delete_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team4',ReceiptHandle=r)

