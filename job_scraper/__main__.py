import boto3

import main 

if __name__ == "__main__":
    boto3.setup_default_session(
        profile_name="admin", region_name="ap-southeast-2"
    )

    main
