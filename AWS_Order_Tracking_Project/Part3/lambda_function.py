"""
LUIT Week 15 Project - AWS Order Tracking System - Part 3
Use Lambda to store the output of the SNS topic to the DynamoDB table, 
along with the date it was posted, and a unique identifier.
Johnny Mac - 24 Apr 2023
"""
import boto3
import json
import uuid
from datetime import datetime

def lambda_handler(event, context):
    #Extract the current time from the SNS event (without parsing as JSON as my initial SNS message is not in JSON format)
    message = event['Records'][0]['Sns']['Message']

    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('OrderNotifications')

    # Generate a unique identifier and timestamp
    notification_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()

    # Store the data in the DynamoDB table
    table.put_item(
        Item={
            'notification_id': notification_id,
            'timestamp': timestamp,
            'message': message
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully saved SNS message: {notification_id}')
    }
