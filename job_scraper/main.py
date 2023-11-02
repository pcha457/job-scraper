from bs4 import BeautifulSoup
import json
import requests


#set variables for url
siteKey = 'NZ-Main'
url = f"https://www.seek.co.nz/api/chalice-search/v4/search?siteKey={siteKey}&sourcesystem=houston&where=All+New+Zealand&page=1&seekSelectAllPages=true&keywords=Data+Engineer&include=seodata&locale=en-NZ"
response = requests.get (url)
data = response.json()["data"]

#connect to slack 
webook = "https://hooks.slack.com/services/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"
headers  = {'Content-type': 'application/x-www-form-urlencoded'}

#adding date filter to below list, only get 1 day before
listing = []

listing_details = {
    listing.append(
        (item ["id"],
        item["title"],
        item["advertiser"]["description"]
        )
        ) for item in data
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

    slack_response = requests.post(webook, json=payload, headers={'Content-type': 'application/json'})
    slack_response.raise_for_status()
#send it to slack




