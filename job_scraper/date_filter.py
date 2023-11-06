from datetime import datetime,timedelta


class DateHelper:

    def date_helper (self,date_str:str):
        # string = data[0]["listingDate"]
        string = date_str.split ("T")[0]
        date_obj = datetime.strptime(string, '%Y-%m-%d')
        return date_obj

    def same_time_yesterday (self):
        date = datetime.today() - timedelta(days=1)
        return date 