import boto3
import botocore.exceptions
import json
import os


class handleDynamodb:
    def __init__(self):
        # is those tables created or not in this region
        # 这里region将会是环境参数来获取
        self.region_name = os.environ['AWS_REGION']
        self.db_client = boto3.client('dynamodb', self.region_name)
        self.response = {}

    def list_tables(self):
        try:
            existed_tables_in_region = self.db_client.list_tables()['TableNames']
        except botocore.exceptions.ClientError as error:
            print(error)
            return
        return existed_tables_in_region
    def table_exists(self, table_name):
        if table_name in self.db_client.list_tables():
            print(f'TableName {table_name} already exists')
            try:
                table_describe = self.db_client.describe_table(TableName=table_name)
                table_status = table_describe['Table']['TableStatus']
                self.response['tableName'] = table_name
                self.response['status'] = 200
                self.response['tableStatus'] = table_status
                self.response['message'] = 'Table already exists and the status is {0}'.format(table_status)
            except botocore.exceptions.ClientError as error:
                print(error)
                self.response['tableName'] = table_name
                self.response['status'] = 500
                self.response['tableStatus'] = 'non-known reason'
                self.response['message'] = 'Table existence is true, however error occur during extract table description'
            return self.response
        else:
            self.response['tableName'] = table_name
            self.response['status'] = 404
            self.response['tableStatus'] = 'non-existed in dynamodb',
            self.response['message'] = 'Table existence is true, however error occur during extract table description'
            return self.response



    def create_table(self, table_definition):
        # create table for those not existed
        definition = table_definition
        tableName = table_definition.TableName
        table_existence = self.table_exists(tableName)
        # check the existence
        if table_existence['status'] == 200:
            return table_existence
        elif table_existence['status'] == 404:
            # This snippet to handle interaction with dynamodb
            try:
                table_creating_response = self.db_client.create_table(
                    TableName=tableName,
                    AttributeDefinitions=definition.KeyAttributeDefinitions,
                    KeySchema=definition.KeyAttributes,
                    Tags=definition.Tags,
                    ProvisionedThroughput={
                        'ReadCapacityUnits': 200,
                        'WriteCapacityUnits': 200
                    },
                )
                waiter = self.db_client.get_waiter('table_exists')
                waiter.wait(
                    TableName=tableName,
                    WaiterConfig={
                        'Delay': 10,
                        'MaxAttempts': 20
                    }
                )
                self.response['tableName'] = tableName
                self.response['status'] = 200
                self.response['tableStatus'] = table_creating_response['TableDescription']['TableStatus'],
                self.response['message'] = 'Table creation successful'
            except botocore.exceptions.ClientError as error:
                print(error)
                self.response['tableName'] = tableName
                self.response['status'] = 500
                self.response['tableStatus'] = 'nonExisted',
                self.response['message'] = 'Error encountered during table creation failed'
        return self.response




    def batchPutItems(self, s3bucket, table_definition):
        # It is designed to get csv source from s3 and then put item by batch
        # before put data in table, should check the existence and readiness
        return {}
