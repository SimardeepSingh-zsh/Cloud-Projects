import boto3
import datetime

# Initialize the AWS Cost Explorer client
ce = boto3.client('ce', region_name='ca-central-1')  # Replace with your region

# Define the time period for the cost data
start_date = datetime.date(2023, 1, 1)  # Replace with your start date
end_date = datetime.date(2023, 12, 31)  # Replace with your end date

# Define the granularity (DAILY, MONTHLY)
granularity = 'DAILY'

# Define the metrics you want to retrieve
metrics = ['BlendedCost', 'UnblendedCost', 'UsageQuantity']

# Query AWS Cost Explorer for cost and usage data
response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': start_date.strftime('%Y-%m-%d'),
        'End': end_date.strftime('%Y-%m-%d')
    },
    Granularity=granularity,
    Metrics=metrics
)

# Print the response (you can process it as needed)
print(response)
