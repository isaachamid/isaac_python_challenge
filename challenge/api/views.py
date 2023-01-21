from django.shortcuts import render
from django.http import HttpResponse

def get_device(request):
    return HttpResponse('Get Device')

def create_device(request):
    return HttpResponse('Create Device')