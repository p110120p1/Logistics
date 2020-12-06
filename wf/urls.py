from wf.view import workflowTypeView
from wf.view import workflowView
from wf.view import workflowStepView
from wf.view import workflowReplaceView
from wf.view import workflowLogView
from django.conf.urls import url

# 定义一个命名空间，与容器中的urls中的命名空间一致

app_name = 'wf'

urlpatterns = [
    # 工作流类型
    url(r'^workflowTypeEntry$', workflowTypeView.workflowTypeEntry, name='workflowTypeEntry'),
    url(r'^findWorkflowTypeEntry$', workflowTypeView.findWorkflowTypeEntry, name='findWorkflowTypeEntry'),
    url(r'^addWorkflowType$', workflowTypeView.addWorkflowType, name='addWorkflowType'),
    url(r'^addWorkflowTypeSave$', workflowTypeView.addWorkflowTypeSave, name='addWorkflowTypeSave'),
    url(r'^editWorkflowType$', workflowTypeView.editWorkflowType, name='editWorkflowType'),
    url(r'^editWorkflowTypeSave$', workflowTypeView.editWorkflowTypeSave, name='editWorkflowTypeSave'),
    url(r'^deleteWorkflowType$', workflowTypeView.deleteWorkflowType, name='deleteWorkflowType'),
    # 工作流信息
    url(r'^workflowEntry$', workflowView.workflowEntry, name='workflowEntry'),



    # 工作流步骤
    url(r'^workflowStepEntry$', workflowStepView.workflowStepEntry, name='workflowStepEntry'),



    # 工作流控制
    url(r'^workflowReplaceEntry$', workflowReplaceView.workflowReplaceEntry, name='workflowReplaceEntry'),



    # 工作流日志
    url(r'^workflowLogEntry$', workflowLogView.workflowLogEntry, name='workflowLogEntry'),
]
