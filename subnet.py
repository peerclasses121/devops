import boto3
from pprint import pprint
ec2 = boto3.client('ec2')
response = ec2.create_subnet(
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    AvailabilityZone='string',
    
    CidrBlock='string',
    
    
    VpcId='string',
    DryRun=True
)

pprint(reponse)