import numpy as np
import pandas as pd
import boto3
import botocore.exceptions
from io import StringIO
import csv

class HandleS3Bucket:
    def __init__(self, event, context):
        self.event = event
        event_region = event['Records'][0]['awsRegion']
        event_time = event['Records'][0]['eventTime']
        event_name = event['Records'][0]['eventName']
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        self.awsRegion = event_region
        self.eventTime = event_time
        self.eventName = event_name
        self.bucket = bucket
        self.key = key
        self.s3_client = boto3.client('s3')


    def getSourcefileContentfromS3(self):
        try:
            response = self.s3_client.get_object(Bucket=self.bucket, Key=self.key)
            file_content = response['Body'].read().decode('utf-8')
            # 使用 Pandas 读取 CSV 数据
            df_content = pd.read_csv(StringIO(file_content))
            print(f'Total number of rows: {df_content.shape[0]}')
            return df_content

        except botocore.exceptions.ClientError as e:
            print(f'error occurred during read {self.key} from {self.bucket} at {self.awsRegion}')
            print(e)
            return None


