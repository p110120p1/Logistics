from django.db.models import Q
from om import models

# 增加数据
def addOmContract(data):
    try:
        models.omOrder.objects.create(**data)
        return True
    except Exception as e:
        print(e)
    return False

# 根据条件模糊查询
def queryOmContract(contractNum,contractName):
    try:
        contractList = models.omOrder.objects.filter(Q(contractNum__startswith=contractNum) & Q(contractName=contractName))
    except Exception as e:
        print(e)
    return contractList
# 根据id查询数据
def queryOmContractById(contractId):
    try:
        contractInfo = models.omOrder.objects.filter(ContractId=contractId).first()
    except Exception as e:
        print(e)
    return contractInfo

# 查询最后一条数据
def queryLastOmContract():
    try:
        contractInfo = models.omOrder.objects.filter().last()
    except Exception as e:
        print(e)
    return contractInfo

# 生成主键
def createContractId():
    contractInfo = queryLastOmContract() # 查询最后一条数据
    if contractInfo:
        ContractId = contractInfo.ContractId # 获取id
        ContractId = int(ContractId) # 先转成int型
        ContractId += 1
        ContractId = str(ContractId) # 再转成str
    else:
        ContractId = '1'
    return ContractId

# 生成申请编号
def createcontractNum():
    contractInfo = queryLastOmContract() # 查询最后一条数据
    if contractInfo:
        contractNum = contractInfo.contractNum # 获取申请编号
        contractNum = int(contractNum) # 先转成int型
        contractNum += 1
        contractNum = str(contractNum) # 再转成str
    else:
        contractNum = '37800001'
    return contractNum

# 编辑后更新数据
def updateOmContract(data):
    ContractId = data['ContractId'] # 根据id更新数据

    if models.omOrder.objects.filter(ContractId=ContractId).update(**data):
        return True
    return False
# 删除数据
def delOmContract(ContractId):
    try:
        models.omOrder.objects.filter(ContractId=ContractId).delete()
    except Exception as e:
        print(e)
        return False
    return True;

