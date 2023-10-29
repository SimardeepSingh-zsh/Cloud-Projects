import boto3
from botocore.exceptions import NoCredentialsError

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except Exception as e:
        print(e)

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        # Enable server-side encryption
        extra_args = {'ServerSideEncryption': 'AES256'}

        # Use a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
        config = boto3.s3.transfer.TransferConfig(
            multipart_threshold=1024 * 25,  # 25MB
            max_concurrency=10,
            num_download_attempts=10,
        )
        transfer = boto3.s3.transfer.S3Transfer(client=s3_client, config=config)
        transfer.upload_file(file_name, bucket, object_name, extra_args=extra_args)
    except NoCredentialsError:
        print("No credentials error")

def download_file(bucket, object_name, file_name):
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket).download_file(object_name, file_name)
    except Exception as e:
        print(e)

# Usage
create_bucket('my-bucket', 'ca-central-1')
upload_file('my-file.txt', 'my-bucket')
download_file('my-bucket', 'my-file.txt', 'downloaded-file.txt')