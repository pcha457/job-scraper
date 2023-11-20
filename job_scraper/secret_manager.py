import boto3
from botocore.exceptions import ClientError
import json


class SecretsHelper():
    def __init__(self):
        """constructor method"""
        # Create a Secrets Manager client
        #remove session when using lambda
        # self.session = boto3.session.Session(profile_name="admin")
        # # #update it to boto3.client
        # self.client = self.session.client(
        #     service_name='secretsmanager',
        #     region_name="ap-southeast-2"
        # )
        self.client = boto3.client("secretsmanager", region_name="ap-southeast-2")
        self.secret_name = "pennyc-slack-webhook"

    def get_secret(self):

        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId=self.secret_name
            )
        except ClientError as e:
            
            raise e

        #get key
        secret = get_secret_value_response['SecretString']
        secret = json.loads(secret)
        secret = secret.get(self.secret_name)

        return secret


