import json
import requests
from date_filter import DateHelper
# import urllib3


class JobScraper:
    def __init__ (self):
        #expend variables for the url 
        self.siteKey = 'NZ-Main'
        self.dt = DateHelper()
        self.listings = set()


    def scrape_list (self) -> set:
        url = f"https://www.seek.co.nz/api/chalice-search/v4/search?siteKey={self.siteKey}&sourcesystem=houston&where=All+New+Zealand&page=1&seekSelectAllPages=true&keywords=Data+Engineer&include=seodata&locale=en-NZ"
        # http = urllib3.PoolManager()
        response = requests.get (url)
        # response = http.request('GET',url)
        data = response.json()["data"]
        

        return set (
            (
                item["id"],
                item["title"],
                item["advertiser"]["description"]
            )
            for item in data 
            if self.dt.same_time_yesterday(number_of_days = 2) < self.dt.date_helper(item["listingDate"])
        )

