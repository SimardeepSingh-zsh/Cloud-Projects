# AWS Cost Explorer Dashboard

This project demonstrates how to fetch AWS cost and usage data using the AWS Cost Explorer API and display insights into your cloud spending. The Python script provided fetches cost and usage data for a specified time period and granularity.

## Prerequisites

1. Python 3.x
2. Boto3 library (`pip install boto3`)
3. AWS CLI configured with appropriate IAM permissions

## Setup

1. Clone the repository:

git clone
cd aws-cost-explorer-dashboard

2. Install the required Python libraries:

3. Configure your AWS CLI with the necessary IAM permissions to access AWS Cost Explorer.

## Usage

1. Open the `cost_explorer.py` script and update the following variables:
- `region_name`: Replace with your AWS region.
- `start_date` and `end_date`: Define the time period you want to analyze.
- `granularity`: Choose the granularity (DAILY or MONTHLY).
- `metrics`: Define the metrics you want to retrieve (e.g., 'BlendedCost', 'UnblendedCost', 'UsageQuantity').

2. Run the Python script:


The script will fetch cost and usage data and print the response.

## Customization

You can extend this project to create a more interactive dashboard using web development frameworks like Flask, Django, or JavaScript libraries like Chart.js or D3.js. This will enable you to visualize and analyze your AWS spending data in a more user-friendly manner.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
