from django.conf.urls import url
from om.view import om_contract_views
app_name = 'om'
urlpatterns = [
    url(r'^addOmContract/$', om_contract_views.addOmContract, name='addOmContract'),
    url(r'^omContractEntry/$', om_contract_views.omContractEntry, name='omContractEntry'),
    url(r'^findOmContract/$', om_contract_views.findOmContract, name='findOmContract'),#查询结算表信息
    url(r'^viewOmContract/$', om_contract_views.viewOmContract, name='viewOmContract'), # 查询某条结算表信息
    url(r'^editOmContract/$', om_contract_views.editOmContract, name='editOmContract'), # 编辑某条结算表信息
    url(r'^delOmContract/$', om_contract_views.delOmContract, name='delOmContract')  # 删除某条结算表信息

]