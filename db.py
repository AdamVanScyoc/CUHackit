#from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')#, endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='DiabetusUsers',
    KeySchema=[
        {
            'AttributeName': 'firstName',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'lastName',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'firstName',
            'AttributeType': 'S' 
        },
        {
            'AttributeName': 'lastName',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Day',
            'AttributeType': 'S'
        },
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

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='DiabetusUsers')

# Print out some data about the table.
print(table.item_count)
