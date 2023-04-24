"""
LUIT Week 15 Project - AWS Order Tracking System - Part 3
Create a DynamoDB table.
Johnny Mac - 24 Apr 2023
"""
import boto3

# Create an AWS DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create a new DynamoDB table
table = dynamodb.create_table(
    TableName='OrderNotifications',
    KeySchema=[
        {
            'AttributeName': 'notification_id',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'timestamp',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'notification_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'timestamp',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

# Wait until the table is created
table.meta.client.get_waiter('table_exists').wait(TableName='OrderNotifications')

print("DynamoDB table created successfully")
