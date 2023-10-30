import os
import boto3
from bs4 import BeautifulSoup
import requests

def lambda_handler(event, context):
    url = 'http://example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv('DYNAMODB_TABLE'))

    # your parsing logic here
    # for example, let's say you're scraping articles and each article has a title and content
    for article in soup.find_all('article'):
        title = article.find('h2').text
        content = article.find('p').text

        table.put_item(
            Item={
                'title': title,
                'content': content
            }
        )