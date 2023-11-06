from bs4 import BeautifulSoup
import json
import requests
from secret_manager import SecretsHelper
from datetime import date, datetime,timedelta
from date_filter import DateHelper

#set variables for url
siteKey = 'NZ-Main'
url = f"https://www.seek.co.nz/api/chalice-search/v4/search?siteKey={siteKey}&sourcesystem=houston&where=All+New+Zealand&page=1&seekSelectAllPages=true&keywords=Data+Engineer&include=seodata&locale=en-NZ"
response = requests.get (url)
data = response.json()["data"]

#connect to slack 
#secrect_name: pennyc-slack-webhook
secrets_helper = SecretsHelper ()
webhook = secrets_helper.get_secret()
headers  = {'Content-type': 'application/x-www-form-urlencoded'}

dt = DateHelper()
listing = []
listing_details = {
    listing.append(
        (item ["id"],
        item["title"],
        item["advertiser"]["description"]
        )
        ) for item in data 
        if dt.same_time_yesterday() < dt.date_helper(item["listingDate"])
        }

for each in listing:
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





