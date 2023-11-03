import boto3
import json
from botocore.exceptions import ClientError


class SecretsHelper():

    def get_secret(self):

        secret_name = "pennyc-slack-webhook"
        region_name = "ap-southeast-2"

        # Create a Secrets Manager client
        session = boto3.session.Session(profile_name="admin")
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            
            raise e

        # Decrypts secret using the associated KMS key.
        secret = get_secret_value_response['SecretString']
        secret = json.loads(secret)
        secret = secret.get(secret_name)

        return secret


