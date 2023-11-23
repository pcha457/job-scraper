import boto3
import json

import main 

if __name__ == "__main__":
    boto3.setup_default_session(
        profile_name="admin", region_name="ap-southeast-2"
    )

    
    with open("job_filter.json") as file:
        filter = json.load(file)
        print (filter)

    for each in filter: 
        main.main(
           country=each.get("country")
        )