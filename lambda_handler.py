"""
Level Up In Tech - week 14 project
Lambda example - stop running Dev EC2 instances on a schedule.
Johnny Mac - 17 Apr 2023
"""
import boto3

def lambda_handler(event, context):
    main()

def get_running_instances(ec2_client):
    response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    return [instance for reservation in response['Reservations'] for instance in reservation['Instances']]

def stop_instances_with_dev_tag(instances, ec2_client):
    for instance in instances:
        if should_stop_instance(instance):
            print(f'Stopping instance: {instance["InstanceId"]}')
            ec2_client.stop_instances(InstanceIds=[instance['InstanceId']])

def should_stop_instance(instance):
    environment_tag_value = get_tag_value(instance, 'Environment')
    instance_name = get_tag_value(instance, 'Name')
    return environment_tag_value == 'Dev' and not instance_name.startswith('aws')

def get_tag_value(instance, tag_key):
    return next((tag['Value'] for tag in instance['Tags'] if tag['Key'] == tag_key), '')

def main():
    ec2_client = boto3.client('ec2')
    running_instances = get_running_instances(ec2_client)
    stop_instances_with_dev_tag(running_instances, ec2_client)
