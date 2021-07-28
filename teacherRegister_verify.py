import requests
import random
import string
import json
import aliyun_oss
base_url='https://tapi-staging.mmears.com'
base_url1='https://apistaging.mmears.com'
telAreaCode_list = ['+1',"+93","+355","+213","+1684","+376"]
first_name = ''
last_name = ''
for i in range(2):
    s = string.ascii_letters
    r = random.choice(s)
    first_name = first_name+r
for i in range(3):
    s = string.ascii_letters
    r = random.choice(s)
    last_name = last_name + r
teacherName=first_name+' '+last_name
headers = {
        "content-type":"application/json;charset=UTF-8",
}
headers1 = {
    "x-app-id":"6"
}

def get_email():
    url = 'http://24mail.chacuo.net/'
    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"__cfduid=d16273138ea3e3ff8108ab2d4c4f1d9e51558753891; yjs_id=a1800577555a6396ad6e48e5afc14d17; bdshare_firstime=1558753892928; yjs_ab_lid=%7B%22data%22%3A%7B%22ip%22%3A%22103.48.232.194%22%2C%22lid%22%3A%2270e4bc15758c38f12cefbacc7e5f5a0844c9%22%2C%22ret_code%22%3A%22300%22%2C%22server_time%22%3A%221560321932556%22%2C%22ver%22%3A%221.0%22%7D%2C%22key_id%22%3A%227%22%2C%22sign%22%3A%22b9ef6e63%22%7D; yjs_ab_score=undefined; cf_clearance=16374014f0dce52aa5c2c8752e3b43ba68ffde61-1560321936-31536000-150; Hm_lvt_24b7d5cc1b26f24f256b6869b069278e=1560950688; Hm_lpvt_24b7d5cc1b26f24f256b6869b069278e=1560950989; ctrl_time=1; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1559531231,1560321937,1561452106; mail_ck=3; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1561452157; sid=4b661825e7c3e5aed79511229920fa9525a190d0"
    }
    data = {
        "data": "kgwiar23816",
        "type": "renew",
        "arg":"d=chacuo.net_f="
    }
    s = requests.post(url = url,params = data,headers = headers)
    # print(s.text)
    s = s.json()
    email_header = s["data"][0]
    email = email_header+'@chacuo.net'
    return email
def teacher_Register():
    try:
        email = get_email()
        url = base_url+"/t/tn/user/register"
        headers = {
            "content-type":"application/x-www-form-urlencoded;charset=UTF-8"
        }
        data = {
            "captcha":'test20210205',
            "email": email,
            "password": "1234qwer",
            "poster":"",
            "referralCode":"",
            "token":""
            # "token": "03AGdBq26e8QiyLsvi4M2-lJKl76yYlJCjPNuTilu-tw2Jm_5_Xt8ugxBm_X7ApOdhWhFiAYpshTu4KP39poQ7iFlpDDpV1DZkBjoP2R_8XGI7wj9ePe58T0DjQv26QnOMMI95WcZ-xzfMvdeSBfjapkC5D2SkeYanx7KBitxU_jeyNRKIY2NaPNoYaasEhLJwqE2Ni_WMGsHNu_BLQdwFcyfJwl7QbYSM_ftpbE9-cRxCEHA09o3oH5Au2-gOnyq6Qqi-m-Yd8GtxAgOBCoty0wt2Kah3oSBUAHz6gictQnMRL-Ycy3MHXkuxCIfUNBVC6-KENlZtzImOylXeqIGFEBZO_e9nreUXHnhCef4TMhZ0Y_f1c3eJcIjq0mJLq5pykFcIpBsvUlC0-JCroAS5d1ypF0IHq5e_HOilxrCdvw8C6dR7ByCFsL6szQ8-DekF7RFtWB8RQaf4jhYqhqfdyht5XCttQasBCg"
        }
        s = requests.post(url=url,data=data,headers=headers)
        s = s.json()
        print(s)
        token = s["data"]["serviceTokenCookie"]["value"]
        teacherId = s["data"]["userIdCookie"]["value"]
        print("老师注册成功！")
        print("注册老师的邮箱：%s \n邮箱密码：1234qwer\n老师id：%s"%(email,teacherId))
        return email,token,teacherId
    except Exception:
        print("注册老师失败！")
t_e = teacher_Register()
email = t_e[0]
token = t_e[1]
teacherId = t_e[2]
headers["x-user-token"]=token
def submit_resume_one(email):
    try:
        telAreaCode = random.choice(telAreaCode_list)
        head = str(random.randint(130,139))
        phoneNum = head + str(random.randint(10000000, 99999999))
        path = '/t/tc/apply/commit/resume/step'
        url = base_url+path
        data = {
            "birthday": "1991/01/19",
            "citizenship": "Canada",
            "commitStep": "1",
            "email": email,
            "firstName": first_name,
            "gender": "MALE",
            "lastName": last_name,
            "middleInitial": None,
            "phoneNum": phoneNum,
            "residency": "Canada",
            "state": "",
            "telAreaCode": telAreaCode
        }
        data = json.dumps(data)
        s = requests.post(url=url,data=data,headers = headers)
        s = s.json()
        code = s["code"]
        if code != "OK":
            submit_resume_one(email)
        print("第一步简历提交成功")
    except Exception:
        print("第一步简历提交失败")
def submit_resume_tow():
    try:
        path = '/t/tc/apply/commit/resume/step'
        url = base_url+path
        data = {
            "commitStep": "2",
            "nativeSpeaker": None,
            "taughtOnline": None,
            "highestLevel": "master’s",
            "teachingCertificate": "Yes",
            "firstLanguage":"ENGLISH",
            "oldTeachingExperience": None
        }
        data = json.dumps(data)
        s = requests.post(url=url,data=data,headers=headers)
        print("第二步简历提交成功")
    except Exception:
        print("第二步简历提交失败")
def submit_resume_three():
    try:
        submit_resume_one(email)
        submit_resume_tow()
        path = "/t/tc/apply/commit/resume/step"
        url = base_url+path
        data = {
            "agree": True,
            "commitStep": "3",
            "fileCVName": None,
            "fileCVUrl": None,
            "hasReferralCode": "NO",
            "heardFromDetail": "",
            "heardMagicEars": "FaceBook",
            "personPhotoBlobUrl": None,
            "personPhotoName": None,
            "personPhotoUrl": None,
            "referralCode": None,
            "whichFriendChannel": None
        }
        data = json.dumps(data)
        s = requests.post(url=url,data=data,headers=headers)
        print("第三步简历提交成功")
    except Exception:
        print("第三步简历提交失败")
def new_login():  #新后台登录
    path = "/auth/login"
    url = base_url1 + path
    data = {
        "code": "123456",
        "email": "bonny@mmears.com",
        "password": "bW1lYXJzMjAxNg=="
    }
    s = requests.post(url=url, data=data)
    token = s.json()["data"]["token"]
    headers1["x-auth-token"] = token
def add_contract():
    try:
        new_login()
        path1='/teacher/apply/get/teacher/citizenship?teacherId={0}'.format(teacherId)
        url1=base_url1+path1
        headers1["content-type"]="application/x-www-form-urlencoded; charset=UTF-8"
        s1=requests.get(url=url1,headers=headers1)
        s1 = s1.json()
        nationality = s1["data"]
        path2='/teacher/pay/contract/predata?teacherId={0}'.format(teacherId)
        url2=base_url1+path2
        s2 = requests.get(url=url2,headers=headers1)
        s2 = s2.json()
        basicIncrease = s2["data"]["basicIncrease"]
        camp = s2["data"]["camp"]
        campValue = s2["data"]["campValue"]
        type = s2["data"]["type"]
        teacherName = s2["data"]["teacherName"]
        peakCarrots = s2["data"]["peakCarrots"]
        path3='/teacher/pay/contract/add'
        url3 = base_url1+path3
        data3 = {
            "basicIncrease": basicIncrease,
            "camp": camp,
            "campValue": campValue,
            "effectTime": "1620230400000",
            "expireTime": "1717689599999",
            "payRuleId": 9,
            "peakCarrots": peakCarrots,
            "teacherId": teacherId,
            "teacherName": teacherName,
            "type": type
        }
        headers1["content-type"]="application/json; charset=UTF-8"
        data3 = json.dumps(data3)
        s3 = requests.post(url=url3,data=data3,headers=headers1)
        s3 = s3.json()
        if s3["code"]=="OK":
            print("老师新增合约成功")
        else:
            print(s3)
    except Exception:
        print("老师新增合约失败")


def activation(teacherId):
    try:
        path='/teacher/info/status/update'
        url = base_url1+path
        headers1["content-type"]="application/json; charset=UTF-8"
        data = {
            "teacherId": teacherId,
            "teacherStatus": "ACTIVE",
            "type": "forever"
        }
        data = json.dumps(data)
        s = requests.post(url=url,data=data,headers=headers1)
        print("激活成功！")
    except Exception:
        print("激活失败")
submit_resume_three()
add_contract()
aliyun_oss.add_certificate(teacherId,fileName='20210414164721.png',filePath='20210414164721.png')
activation(teacherId)