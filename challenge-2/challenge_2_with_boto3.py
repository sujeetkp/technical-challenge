import boto3
import json

instance_id = input("Enter Instance ID: ")

#instance_id = 'i-0d860c15f9cac2ef0'

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

# Print in JSON
print(json.dumps(response, indent=2, default=str))

##########################

attribute = input("Enter Attribute path as slash separated: ")

#attribute = 'Placement/AvailabilityZone'

keys = attribute.split('/')
value = f'''response['Reservations'][0]['Instances'][0]'''

for key in keys:
    value = value + ".get('" + key + "')"

value = 'print(' + value + ')'

#print(value)

exec(value)

