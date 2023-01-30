from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APISimpleTestCase


client = APIClient()

class TestGetDevice(APISimpleTestCase):

    def test_case1_get_device_valid(self):
        response = client.get("http://localhost:8000/api/v1/devices/id1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_case2_get_device_invalid(self):
        response = client.get("http://localhost:8000/api/v1/devices/id999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class Test_CreateDevice(APISimpleTestCase):

    def setUp(self):
        self.payload1_valid = {
            "id": "/devices/id16",
            "deviceModel": "/devicemodels/id1",
            "name": "Sensor1",
            "note": "Testing a sensor1.",
            "serial": "A020000101",
        }

        self.payload2_invalid = {
            "id": "", # id required field
            "deviceModel": "/devicemodels/id2",
            "name": "", # name required field
            "note": "Testing a sensor2.", 
            # serial required field
        }

        self.payload3_invalid = {
            "id": "3", # /devices/id<pk>
            "deviceModel": "/devicemodels/id3",
            "name": "Sensor3",
            "note": "Testing a sensor3.",
            "serial": "A020000103",
        }

        self.payload4_invalid = {
            "id": "3", # /devices/id<pk>
            "deviceModel": "/devicemodels/id3",
            "name": 123,
            "note": "Testing a sensor3.",
            "serial": "A020000103",
        }

    def test_case1_create_device_valid(self):
        response = client.post("http://localhost:8000/api/v1/devices/", self.payload1_valid)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_case2_create_device_invalid(self):
        response = client.post("http://localhost:8000/api/v1/devices/", self.payload2_invalid)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_case3_create_device_invalid(self):
        response = client.post("http://localhost:8000/api/v1/devices/", self.payload3_invalid)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_case4_create_device_invalid(self):
        response = client.post("http://localhost:8000/api/v1/devices/", self.payload4_invalid)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_case5_create_device_invalide(self):
        response = client.post("http://localhost:8000/api/v1/devices/", self.payload1_valid)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)