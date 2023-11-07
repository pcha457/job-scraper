import boto3
from botocore.exceptions import ClientError

class DynamoHelper:
    """Encapsulates an Amazon DynamoDB table of movie data."""

    def __init__(self):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.session = boto3.session.Session(profile_name="admin")
        self.dynamodb = self.session.resource(
            service_name='dynamodb',
            region_name="ap-southeast-2"
        )
        # The table variable is set during the scenario in the call to
        # 'exists' if the table exists. Otherwise, it is set by 'create_table'.
        self.table = self.dynamodb.Table('job-listing')

    def add_data(self, id, title, company):
        """
        Lists the Amazon DynamoDB tables for the current account.

        :return: The list of tables.
        """
        try:
            response = self.table.put_item (
                Item={
                    "id": id,
                    "title": title,
                    "company": company
                }

            )
        except ClientError as err:
            
            raise err