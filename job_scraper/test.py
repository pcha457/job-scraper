from bs4 import BeautifulSoup
import json
import requests
from secret_manager import SecretsHelper
from datetime import date, datetime,timedelta
from date_filter import DateHelper
from dynamo_helper import DynamoHelper
from job_scraper import JobScraper
import datetime
import logging


def main():
    #connect to slack 
    #secrect_name: pennyc-slack-webhook
    secrect = SecretsHelper ()
    webhook = secrect.get_secret()
    headers = {'Content-type': 'application/x-www-form-urlencoded'},

    scraper = JobScraper ()
    listing = scraper.scrape_list ()
    print (listing)

    #function that adding the list to dynamodb 
    db = DynamoHelper ()
    for each in listing:
    #saving listing to the dynamodb
        db.add_data(each [0], each[1], each[2])
    #create payload for slack
        payload = {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"{each[1]}"
                            f"\n Advertiser: {each[2]}"
                        }
            }
        ]
    }
    # #send it to slack
        slack_response = requests.post(webhook, json=payload, headers={'Content-type': 'application/json'})
        slack_response.raise_for_status()



def lambda_handler(event, context):
    main()


