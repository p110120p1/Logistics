from django.shortcuts import render
import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from wf.models import wfWorkflowType
from wf.models import wfWorkflow
from django.forms.models import model_to_dict
from tools import shareMethodHelper
import time
import datetime
# Create your views here.

# 主页面
@login_required
@xframe_options_exempt
def workflowTypeEntry(request):
    return render(request,'wf/workflowTypeEntry.html')

# 主页面信息查询
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


# 添加页面
@login_required
@xframe_options_exempt
def addWorkflowType(request):
    workflows = wfWorkflow.objects.filter()
    return render(request,'wf/addWorkflowType.html',{'workflows':workflows})


# 添加保存
@login_required
@xframe_options_exempt
def addWorkflowTypeSave(request):
    orderType = request.POST.get('orderType')
    workflowId = request.POST.get('workflowId')
    companyId = request.POST.get('companyId')
    deptId = request.POST.get('deptId')
    createUserId = request.POST.get('createUserId')
    updateUserId = request.POST.get('updateUserId')
    delFlag = request.POST.get('delFlag')
    # 生成ID
    WorkflowTypeId = 2020001000
    for i in range(999999999):
        if len(wfWorkflowType.objects.filter(WorkflowTypeId=WorkflowTypeId)):
            WorkflowTypeId += 1
        else:
            break

    '2020-12-05 22:12:39.178561'
    createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    updateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    createTime1 = str(createTime)
    createTime2 = '.178561'
    createTime = createTime1 + createTime2
    print("---------------------")
    print(createTime)
    print("---------------------")
    # 开始保存
    aworkflowtype = wfWorkflowType()
    aworkflowtype.WorkflowTypeId = WorkflowTypeId
    aworkflowtype.orderType = orderType
    # 外键需要传对象
    aworkflow = wfWorkflow.objects.get(WorkflowId=workflowId)
    aworkflowtype.workflowId = aworkflow
    aworkflowtype.companyId = companyId
    aworkflowtype.deptId = deptId
    aworkflowtype.createUserId = createUserId
    aworkflowtype.updateUserId = updateUserId
    aworkflowtype.delFlag = delFlag
    aworkflowtype.createTime = createTime
    aworkflowtype.updateTime = str(updateTime)
    aworkflowtype.save()
    return render(request,'wf/workflowTypeEntry.html')


@login_required
@xframe_options_exempt
def editWorkflowType(request):
    return render(request,'wf/editWorkflowType.html')

