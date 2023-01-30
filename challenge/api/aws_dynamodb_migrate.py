import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv
load_dotenv()


def aws_create_table():
  dynamodb = boto3.client(
      "dynamodb",
      aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
      aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
      region_name = os.getenv("AWS_REGION_NAME")
  )

  response = dynamodb.create_table(
    TableName = os.getenv("TABLE_NAME"),
    AttributeDefinitions = [
      {
        "AttributeName": "id",
        "AttributeType": "S"
      }
    ],
    KeySchema = [
      {
        "AttributeName": "id",
        "KeyType": "HASH"
      }
    ],
    ProvisionedThroughput = {
      "ReadCapacityUnits": 1,
      "WriteCapacityUnits": 1
    }
  )

  return response


try:
    print("******************* Start Creating Table On AWS *******************")
    aws_create_table()
    print("Table created successfully.")
except ClientError as e:
    print("******************* Something Went Wrong! *******************")
    if e.response["Error"]["Code"] == "ResourceInUseException":
        print("Table already exists")
    else:
        print("Unexpected error: %s" % e)