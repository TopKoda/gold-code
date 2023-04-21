"""
LUIT Week 15 Project - AWS Order Tracking System - Part 1
Programatically poll messages in the SQS queue to verify they were sent correctly.
Johnny Mac - 20 Apr 2023
"""
import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Set our SQS Queue URL
queue_url = 'https://sqs.eu-west-2.amazonaws.com/954189283900/CustomerOrderNotifications'

# Receive the message from the SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1
)

if 'Messages' in response:
    message = response['Messages'][0]
    print(f"Message ID: {message['MessageId']}, Content: {message['Body']}")
    # Delete the message after processing
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )
else:
    print("No messages in the queue")
