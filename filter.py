import boto3
client = boto3.client('ec2')
response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'Webserver',
            ]
        },
    ],
    DryRun=True
)

print(response)