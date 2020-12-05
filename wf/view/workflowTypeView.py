from django.shortcuts import render
import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from wf.models import wfWorkflowType
from django.forms.models import model_to_dict
from tools import shareMethodHelper
# Create your views here.


@login_required
@xframe_options_exempt
def workflowTypeEntry(request):
    return render(request,'wf/workflowTypeEntry.html')


@login_required
@xframe_options_exempt
def findWorkflowTypeEntry(request):
    pageSize = request.GET.get('pageSize')
    pageNumber = request.GET.get('pageNumber')
    pageSize = int(pageSize)
    pageNumber = int(pageNumber)
    print("---------------------")
    print(pageNumber)
    print("---------------------")
    workflowTypeList = wfWorkflowType.objects.filter()# 查询结果为queryset




    # 分页
    totalLength = len(workflowTypeList)  # 查询结果的总长度
    workflowTypeListPage = workflowTypeList[(pageNumber - 1) * pageSize:(pageNumber) * pageSize]  # 一页显示的数据
    datas = []  # 存储查询结果的列表
    for i in range(len(workflowTypeList)):
        # data['WorkflowTypeId'] = shareMethodHelper.dateToStr(data['WorkflowTypeId'])  # 注意：时间需要转换下
        data = {}
        data['WorkflowTypeId'] = workflowTypeList[i].WorkflowTypeId
        data['orderType'] = workflowTypeList[i].orderType
        data['workflowId'] = workflowTypeList[i].workflowId.WorkflowId
        datas.append(data)  # 将字典添加到list中
    return HttpResponse(json.dumps({'total': totalLength, 'rows': datas}),
                        content_type='application/json')  # total rows 必须叫这个名字
