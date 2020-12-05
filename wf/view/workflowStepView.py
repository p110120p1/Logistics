from django.shortcuts import render
import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.


@login_required
@xframe_options_exempt
def workflowStepEntry(request):
    return HttpResponse('ok')