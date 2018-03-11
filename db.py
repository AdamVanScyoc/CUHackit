from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')#, endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='DiabetusUsers',
    KeySchema=[
        {
            'AttributeName': 'Day',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Glucose',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'CarbIntake',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Insulin',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Hours',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Min',
            'AttributeType': 'N'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 30,
        'WriteCapacityUnits': 30
    }
)

print("Table status:", table.table_status)

