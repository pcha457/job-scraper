import json
import requests
# from botocore.vendored import requests
from datetime import date, datetime, timedelta
from .date_filter import DateHelper
# from dynamo_helper import DynamoHelper
from .job_scraper import JobScraper
from .slack_helper import SlackHelper
import datetime
import logging


def main(country:str):
    #connect to slack 
    #secrect_name: pennyc-slack-webhook

    scraper = JobScraper (country)
    listing = scraper.scraping_all_pages ()
    print (listing)

    #function that adding the list to dynamodb 
    # db = DynamoHelper ()

    #slack notification
    job_notify = SlackHelper()
    if len(listing) == 0:
        text = "No jobs listed today"
        job_notify.notify_none (text)

    # #send it to slack
    job_notify.notify_new_listings (listing, country)

def lambda_handler(event, context): 
    with open("job_scraper/job_filter.json") as file:
        filter = json.load(file)
        print (filter)

    for each in filter: 
        main(
           country=each.get("country")
        )

