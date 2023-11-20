import requests
from secret_manager import SecretsHelper

class SlackHelper():
    def __init__(self):
        """constructor method"""
        self.headers = {'Content-type': 'application/x-www-form-urlencoded'}
        self.secrect = SecretsHelper ()


    def send_slack_message(self, webhook: str, json: str) -> int:
        """ Sends slack message

        Arguments:
            webhook {str} -- slack url connection
            payload {str} -- json document for job listing
        """
        try:
            slack_response = requests.post(
                url=webhook, 
                json=json, 
                headers=self.headers
            )
            slack_response.raise_for_status
            #if an error occur, this returns a below HTTPError object
        except requests.exceptions.HTTPError as e:
            if status_code == 403:
                print("Invalid slack url")
            else:
                return status_code

    def notify_new_listings (self, listings: list) -> None:
        
        """job notify on slack channal
        
        Arguments:
            listings {list} -- listing from web scraping

        """
        for each in listings:
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
            
            webhook = self.secrect.get_secret()
            self.send_slack_message (webhook, payload)
    
    def notify_none (self, text: str) -> None:
        """
        notify if there is no jobs today 

        """
        message = {
            "blocks": [
                {
    		"type": "section",
    		"block_id": "section567",
    		"text": {
    			"type": "mrkdwn",
    			"text": f"{text}"
    		}
                }

    ]
}

        webhook = self.secrect.get_secret()
        self.send_slack_message (webhook, message)

        