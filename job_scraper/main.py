import json
import requests
from datetime import date, datetime,timedelta
from date_filter import DateHelper
from dynamo_helper import DynamoHelper
from job_scraper import JobScraper 
from slack_helper import SlackHelper
import datetime
import logging


def main():
    #connect to slack 
    #secrect_name: pennyc-slack-webhook

    scraper = JobScraper ()
    listing = scraper.scraping_all_pages ()
    print (listing)

    #function that adding the list to dynamodb 
    # db = DynamoHelper ()
    job_notify = SlackHelper()
    if len(listing) == 0:
        text = "No jobs in these two days"
        job_notify.notify_none (text)

    # #send it to slack
    # job_notify = SlackHelper()
    job_notify.notify_new_listings (listing)

def lambda_handler(event, context):
    main()
   

main()