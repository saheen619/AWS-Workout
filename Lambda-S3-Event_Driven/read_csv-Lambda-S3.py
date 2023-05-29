# To get_object from s3 using lambda
# To read_csv from s3 using pandas in lambda


import boto3
import pandas as pd

client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        s3_filename = event['Records'][0]['s3']['object']['key']
        response = client.get_object(Bucket=bucket, Key=s3_filename)
        print(response['Body'])
        df_data = pd.read_csv(response['Body'], sep = ',')
        print(df_data.head())
    except Exception as err:
        print(err)