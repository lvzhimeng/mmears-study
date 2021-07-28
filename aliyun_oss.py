import requests
import oss2
import json
import datetime
headers= {
    "x-app-id":"6",
}
objectName = None
securityToken = None
accessKeyId = None
accessKeySecret = None
param={

}
base_url="https://apistaging.mmears.com"
def cc_login():
    try:
        url = base_url+"/auth/login"
        data = {
            "code": "123456",
            "email": "bonny@mmears.com",
            "password": "bW1lYXJzMjAxNg=="
        }
        s = requests.post(url=url,data=data)
        token = s.json()["data"]["token"]
        headers["x-auth-token"]=token
        print("新后台登录成功")
    except Exception:
        print("新后台登录失败")
def get_object(teacherId,fileName,resourceType):
    url = base_url+'/teacher/oss/upload/private/object'
    data = {
        "teacherId": teacherId,
        "fileName": fileName,
        "resourceType": resourceType,
        "operateType": "WRITE_OPERATE",
        "operator": "MMEARS_OPERATOR"
    }
    headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    s = requests.post(url=url,data=data,headers=headers)
    s = s.json()
    global objectName,securityToken,accessKeyId,accessKeySecret
    objectName = s["data"]["objectName"]
    securityToken = s["data"]["securityToken"]
    accessKeyId = s["data"]["accessKeyId"]
    accessKeySecret = s["data"]["accessKeySecret"]
    if resourceType=="TEACHER_CERTIFICATE_ACADEMIC":
        param["academicCertificateName"]=fileName
        param["academicCertificateType"]="JPG"
        param["academicCertificateUrl"] = objectName
    elif resourceType=="TEACHER_CERTIFICATE_TEACHING":
        param["teachingCertificateName"]=fileName
        param["teachingCertificateType"] = "JPG"
        param["teachingCertificateUrl"] = objectName
    elif resourceType=="TEACHER_PROOF_CERTIFICATE":
        param["proofCertificateName"]=fileName
        param["proofCertificateType"] = "JPG"
        param["proofCertificateUrl"] = objectName
    elif resourceType=="TEACHER_CERTIFICATE_IDENTITY":
        param["identifyCertificateName"]=fileName
        param["identifyCertificateType"] = "JPG"
        param["identifyCertificateUrl"] = objectName
def update_photo(filePath):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    t = datetime.datetime.utcnow().strftime(GMT_FORMAT)
    headers1  ={
        "x-oss-security-token":securityToken,
        "x-oss-date":t,
        "x-oss-user-agent":"aliyun-sdk-js/6.15.1 Chrome 89.0.4389.90 on OS X 10.14.6 64-bit",
        "Content-Type":"image/png"
    }
    auth = oss2.Auth(access_key_id=accessKeyId,access_key_secret=accessKeySecret)
    bucket = oss2.Bucket(auth=auth, endpoint='https://oss-cn-beijing.aliyuncs.com', bucket_name= 'mmears-staging-private')
    bucket.put_object_from_file(key = objectName,filename= filePath,headers=headers1)
def submit(teacherId):
    try:
        url = base_url+"/teacher/certificate/update/teacher"
        param["teacherId"] = teacherId
        data = json.dumps(param)
        headers["content-type"]="application/json"
        s = requests.post(url=url,data=data,headers=headers)
        print("提交证书成功")
    except Exception:
        print("提交证书失败")
def check_certificate(teacherId,certificateType):
    url = base_url+'/teacher/apply/resource/update/check?teacherId={0}&status=PASS&useType={1}'.format(teacherId,certificateType)
    headers["content-type"]="application/x-www-form-urlencoded; charset=UTF-8"
    s = requests.get(url=url,headers=headers)


def add_certificate(teacherId,fileName,filePath):
    cc_login()
    resourceType_list = ["TEACHER_CERTIFICATE_ACADEMIC", "TEACHER_CERTIFICATE_TEACHING", "TEACHER_PROOF_CERTIFICATE",
                         "TEACHER_CERTIFICATE_IDENTITY"]
    certificateType_list = ["TEACHER_CERTIFICATE", "PASSPORT", "PROOF_CERTIFICATE", "EDU_CERTIFICATE"]
    try:
        for i in resourceType_list:
            get_object(teacherId=teacherId, fileName=fileName, resourceType=i)
            update_photo(filePath=filePath)
        print("上传图片成功")
    except Exception:
        print("上传图片失败")
    submit(teacherId=teacherId)
    try:
        for i in certificateType_list:
            check_certificate(teacherId=teacherId, certificateType=i)
        print("审核证书成功")
    except Exception:
        print("审核证书失败")
if __name__=='__main__':
    add_certificate(teacherId='1225080',fileName='20210414164721.png',filePath='20210414164721.png')
