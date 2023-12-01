import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Create a session using your AWS credentials
aws_session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-west-2'
)

# Create an EC2 resource object using the AWS session
ec2_resource = aws_session.resource('ec2')

def create_security_group(group_name, description):
    """
    Create a security group
    """
    try:
        security_group = ec2_resource.create_security_group(
            GroupName=group_name,
            Description=description
        )
        print(f'Security Group Created {security_group.id} in vpc {security_group.vpc_id}.')
    except ClientError as e:
        print(f'Error: {e}')
    return security_group

def add_inbound_rule_to_sg(security_group):
    """
    Add inbound rule to security group
    """
    try:
        data = security_group.authorize_ingress(
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        print('Ingress Successfully Set %s' % data)
    except ClientError as e:
        print(f'Error: {e}')

# Usage
sg = create_security_group("test_sg", "Test security group")
add_inbound_rule_to_sg(sg)