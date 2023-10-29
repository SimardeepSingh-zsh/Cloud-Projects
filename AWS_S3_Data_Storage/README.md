# Cloud-Based Data Storage and Retrieval

This project provides a simple example of a cloud-based data storage and retrieval system using Amazon Web Services (AWS) S3 and Python's boto3 library.

## Prerequisites

- Python 3.6 or later
- boto3 library
- An AWS account
- AWS credentials configured (You can do this by setting the following environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` if you are using temporary security credentials)

## Usage

1. Replace `'my-bucket'`, `'us-west-2'`, `'my-file.txt'`, and `'downloaded-file.txt'` in the script with your actual AWS S3 bucket name, AWS region, file to upload, and downloaded file name respectively.
2. Run the script.

## Functions

- `create_bucket`: Creates a new bucket in the specified region. If no region is specified, the bucket is created in the S3 default region.
- `upload_file`: Uploads a file to the specified bucket.
- `download_file`: Downloads a file from the specified bucket.