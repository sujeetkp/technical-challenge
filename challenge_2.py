import boto3
import json

#instance_id = input("Enter Instance ID: ")
#attribute = input("Enter Attribute path in Slash separated: ")

instance_id = 'i-0d860c15f9cac2ef0'
attribute = 'Placement/AvailabilityZone'

client = boto3.client('ec2')

'''
response = client.describe_instances(
    InstanceIds=[
        'i-0d860c15f9cac2ef0'
    ]
)
'''

response = client.describe_instances(
    InstanceIds=[
        instance_id
    ]
)

#print(json.dumps(response, indent=2, default=str))

keys = attribute.split('/')
value = f'''response['Reservations'][0]['Instances'][0]'''

for key in keys:
    value = value + ".get('" + key + "')"

value = 'print(' + value + ')'

#print(value)

exec(value)

