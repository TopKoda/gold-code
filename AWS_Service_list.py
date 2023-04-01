"""
Simple Python code to demonstrate lists
Johnny Mac - 01 Apr 2023
"""

# create and empty list
aws_services_list = []

# populate list with AWS Services
aws_services_list.append("DynamoDB")
aws_services_list.append("EC2")
aws_services_list.append("Lambda")
aws_services_list.append("RDS")
aws_services_list.append("S3")

# print the list and its length
print(f"Starting AWS Services list: {aws_services_list}")
print(f"Starting AWS Services list length: {len(aws_services_list)}")

# remove two services from the list
aws_services_list.remove("DynamoDB")
aws_services_list.remove("S3")

# print the updated list and its length
print(f"Revised AWS Services list: {aws_services_list}")
print(f"Revised AWS Services list length: {len(aws_services_list)}")