from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from api.dynamo_models import Device
from .serializer import DeviceSerializer
import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv
load_dotenv()

dynamodb = boto3.client(
    "dynamodb",
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name = os.getenv("AWS_REGION_NAME")
)

class DynamoRequest(APIView):
    #GET Device List
    def get(self, request):
        try:
            response = []
            items = dynamodb.scan(TableName = os.getenv("TABLE_NAME"))["Items"]
            if items:
                for item in items:
                    device = Device(item["id"]["S"], item["deviceModel"]["S"], item["name"]["S"], item["note"]["S"], item["serial"]["S"])
                    response.append(device.__dict__)
                return Response(status=status.HTTP_200_OK, data=response)
            else:
                return Response(status=status.HTTP_200_OK, data={"message": "There is no device."})
        except ClientError as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "Unexpected error: %s" % e})

    #POST Device
    def post(self, request):
        try:
            request_data = request.data
            # validate request
            serializer = DeviceSerializer(data=request_data)
            if serializer.is_valid():
                # check duplicate device
                item = dynamodb.get_item(
                    TableName = os.getenv("TABLE_NAME"),
                    Key = {
                        "id":  {"S": request_data["id"]}
                    }
                )
                if "Item" in item:
                    return Response(status=status.HTTP_409_CONFLICT, data={'message': f'Device already exists, id: {request_data["id"]}.'})
                else:
                    item = {
                        "id":{"S":request_data["id"]},
                        "deviceModel":{"S":request_data["deviceModel"]},
                        "name":{"S":request_data["name"]},
                        "note":{"S":request_data["note"]},
                        "serial":{"S":request_data["serial"]}
                    }

                    dynamodb.put_item(
                        TableName = os.getenv("TABLE_NAME"),
                        Item = item
                    )
                    return Response(status=status.HTTP_201_CREATED, data=request_data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        except ClientError as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "Unexpected error: %s" % e})


class DynamoDetailRequest(APIView):
    #GET Device
    def get(self, request, pk):
        try:
            item = dynamodb.get_item(
                TableName = os.getenv("TABLE_NAME"),
                Key = {
                    "id":  {"S": f"/devices/id{pk}"}
                }
            )
            if "Item" in item:
                item = item["Item"]
                device = Device(item["id"]["S"], item["deviceModel"]["S"], item["name"]["S"], item["note"]["S"], item["serial"]["S"])
                return Response(status=status.HTTP_200_OK, data=device.__dict__)
        except ClientError as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "Unexpected error: %s" % e})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Device Not Found."})