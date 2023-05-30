import boto3
import json

client = boto3.client('sns')

snsARN = '<ARN>'

def lambda_handler(event, context):
    message = 'Hi, This message is from AWS S3. The file put with suffux .csv succeeded'
    
    response = client.publish(
        TargetArn = snsARN,
        Message = message,
        Subject = 'Message from AWS S3',
        MessageStructure = 'string'
    )
    print(response)