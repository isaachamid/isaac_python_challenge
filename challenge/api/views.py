from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from api.models import Device


class GetDeviceAPIView(APIView):
    def get_device(self, request, pk):
        return Response(status=status.HTTP_200_OK, data={'message': 'Get Device'})

class CreateDeviceAPIView(APIView):
    def create_device(self, request):
        return Response(status=status.HTTP_200_OK, data={'message': 'Create Device'})
