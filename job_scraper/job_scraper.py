import json
import requests
from date_filter import DateHelper
# import urllib3


class JobScraper:
    def __init__ (self, country):
        #expend variables for the url 
        self.country = country
        self.dt = DateHelper()
        #empty set for looping pages
        self.listings = set()


    def scrape_list (self, page) -> set:
        """

        """
        #creating a nesting Dictionary to store 
        country_dic ={
            "NZ": {
                "siteKey": "NZ-Main", 
                "where": "All+New+Zealand"
                },
            "AU": {
                "siteKey": "AU-Main", 
                "where": "All+Australia"
            }

        }
        siteKey = country_dic.get(self.country).get("siteKey")
        where = country_dic.get(self.country).get("where")

        url = f"https://www.seek.co.nz/api/chalice-search/v4/search?siteKey={siteKey}&sourcesystem=houston&where={where}&page={page}&seekSelectAllPages=true&keywords=Data+Engineer&include=seodata&locale=en-NZ"
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
    
    def scraping_all_pages (self):
        """
        Get all page listing 

        return:
            {set} -- An union collections of ids, title, advertiser 

        """
        #set init page value to 1
        current_page = 1 
        while True:
            # assume second time self.listings end as 2 
            # when starting the third time, current_listing will equal to 2 as the second time
            current_listing = self.listings
            # new listing is 0 
            current_page_listing = self.scrape_list (current_page)
            # adding 0 to 2 as new self.listings
            self.listings = current_listing.union(current_page_listing)
            # current_listing from 2nd is 2, 3rd self.listings is also 2 
            if current_listing == self.listings:
                return current_listing
                break
            current_page += 1 

    # def expend_job_list (self):


            


        


