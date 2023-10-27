import boto3
import logging
import sys

# Initialize the AWS CloudWatch Logs client
client = boto3.client('logs', region_name='your-region')

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a log group
log_group_name = 'my-log-group'
client.create_log_group(logGroupName=log_group_name)

# Create a log stream
log_stream_name = 'my-log-stream'
client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)

# Log messages
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.addHandler(logging.handlers.CloudWatchLogHandler(client, log_group_name, log_stream_name))
logger.info('This is a log message.')
