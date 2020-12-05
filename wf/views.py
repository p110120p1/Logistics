from django.shortcuts import render
import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def wftest1(request):
    return HttpResponse('ok')