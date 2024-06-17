import json
import boto3
import botocore.exceptions
import os

from tableDefinitions import tableFactory
from handleDynamodb import handleDynamodb
from handleS3Bucket import HandleS3Bucket


def lambda_handler(event, context):


    '''
     Extract key params from s3 event notification, and if yes, start to insert data into proper table
     Conventions:
     1, Must be:  family id and table name should be included in table content in columns.  if there are no those 2 columns,
        lambda function will stop without notification
     2, Table types should be defined in tableDefinitions.py in lambda function,
        if there is non-consistence on table type between in csv file and table definition, lambda function will stop without notification
    '''
    source_in_s3 = HandleS3Bucket(event, context).getSourcefileContentfromS3()
    if ((type(source_in_s3) != 'NoneType') &
            ('TABLE_TYPE' in source_in_s3.columns) &
            ('FAMILY_ID' in source_in_s3.columns) &
            (source_in_s3.shape[0] > 0)):
            table_type = source_in_s3['TABLE_TYPE'].to_list()[0]   ### ！！！这里一定要注意
            family_id = source_in_s3['FAMILY_ID'].to_list()[0]
            tableDefinitions = tableFactory().tableDefinition(table_type, family_id)
            if type(tableDefinitions) != 'NoneType':
                table_name = list(tableDefinitions.keys())[0]
                db_handler = handleDynamodb()
                response = db_handler.batchPutItemsOrCreate(table_name, tableDefinitions,source_in_s3)
                return {
                    "statusCode": 200,
                    "body": json.dumps({
                        "message": response
                    }),
                }
            else:
                return {
                    "statusCode": 500,
                    "body": json.dumps({
                        "message": 'The table type is not consistent with what we has specified.'
                    }),
                }
    return {
        "statusCode": 500,
        "body": json.dumps({
            "message": 'TABLE TYPE and FAMILY ID should be included in table content.'
        }),
    }
