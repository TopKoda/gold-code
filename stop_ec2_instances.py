"""
LUIT Week 14 Project - using Python to stop EC2 instances

Johnny Mac - 13 Apr 2023
"""
import boto3

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

if __name__ == "__main__":
    main()
