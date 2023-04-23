"""
LUIT Week 15 Project - AWS Order Tracking System - Part 2
Create an SNS topic.
Johnny Mac - 23 Apr 2023
"""
import boto3

# Create an SNS client
sns = boto3.client('sns')

# Create a new SNS Topic
response = sns.create_topic(Name='OrderShippedNotificationTopic')

# Get the Topic ARN (Amazon Resource Name)
topic_arn = response['TopicArn']

print(f"Created SNS Topic with ARN: {topic_arn}")
