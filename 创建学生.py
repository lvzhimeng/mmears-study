# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 11:40
# @Author  : lvzhimeng
# @FileName: 创建学生.py
# @Software: PyCharm
import json

import requests
import string,random
base_url = "https://apistaging.mmears.com"
headers = {
    "x-app-id": "1"
}
telAreaCode_list = ['1',"968","971","852","353","213"]
first_name = ''
countryCode = random.choice(telAreaCode_list)
head = str(random.randint(130, 139))
phoneNum = head + str(random.randint(10000000, 99999999))
print("学生号码：%s,号码区号：%s"%(countryCode,phoneNum))
for i in range(4):
    s = string.ascii_letters
    r = random.choice(s)
    first_name = first_name+r
studentName=first_name
def cc_login():
    path = "/auth/login"
    url = base_url+path
    data = {
        "code": "123456",
        "email": "bonny@mmears.com",
        "password": "bW1lYXJzMjAxNg=="
    }
    s = requests.post(url=url,data=data)
    token = s.json()["data"]["token"]
    headers["x-auth-token"]=token
def saveStudent():
    try:
        path = "/customer/studentocean/savestudent"
        url = base_url+path

        headers["content-type"] = "application/json;charset=UTF-8"

        data = {
            "age": 5,
            "birthDate": "2016-04-30T16:00:00.000Z",
            "birthMonth": "05",
            "birthYear": "2016",
            "ccId": 839,
            "contactPhone": phoneNum,
            "countryCode": countryCode,
            "gender": "UNKNOWN",
            "level": 1,
            "month": 0,
            "nickName": studentName,
            "specialLevel": 1,
            "unit": 201
        }
        data = json.dumps(data)
        s = requests.post(url=url,data=data,headers=headers)
        s = s.json()
        print("添加学生成功")
    except Exception:
        print('添加学生失败')
def get_studentId(phoneNum):
    path =  "/customer/info/search/student"
    url = base_url+path
    # headers["content-type"]= 'application/x-www-form-urlencoded;charset=UTF-8'
    data = {
        "searchKey": phoneNum
    }
    s= requests.get(url=url,params=data,headers=headers)
    s = s.json()
    studentId = s["data"]
    print("学生id：%s"%studentId)
    return studentId
def add_coursePackage(phoneNum,productId=197):  #197固班
    studentId = get_studentId(phoneNum)
    try:
        path = "/shop-service/order/check/condition"
        path1 = "/shop-service/order/add/finish/order"
        url = base_url+path
        url1 = base_url+path1
        headers["content-type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        data = {
            "studentId": studentId,
            "paymentId": 3,
            "productId": productId
        }
        data1 = {
            "studentId": studentId,
            "paymentId": 3,
            "productId": productId
        }
        s = requests.post(url=url,data=data,headers=headers)
        s1 = requests.post(url=url1,data=data1,headers=headers)
        s = s.json()
        s1 = s1.json()
        print("添加课包成功")
    except Exception:
        print("添加课包失败")

cc_login()
saveStudent()
# add_coursePackage(phoneNum)
