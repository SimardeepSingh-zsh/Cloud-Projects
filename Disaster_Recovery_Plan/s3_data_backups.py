import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Create an S3 bucket for backups
s3.create_bucket(Bucket='my-dr-backups')

# Enable versioning for the S3 bucket
s3.put_bucket_versioning(
    Bucket='my-dr-backups',
    VersioningConfiguration={
        'Status': 'Enabled'
    }
)

# Configure a lifecycle policy for the S3 bucket to transition objects to Glacier
s3.put_bucket_lifecycle_configuration(
    Bucket='my-dr-backups',
    LifecycleConfiguration={
        'Rules': [
            {
                'ID': 'Archive to Glacier',
                'Status': 'Enabled',
                'Prefix': '',
                'Transitions': [
                    {
                        'Days': 30,
                        'StorageClass': 'GLACIER'
                    }
                ]
            }
        ]
    }
)
