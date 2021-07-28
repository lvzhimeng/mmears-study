# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 15:58
# @Author  : lvzhimeng
# @FileName: 老师后台添加stb课程.py
# @Software: PyCharm
import requests
import time,datetime
import json
import math
r = requests.session()
base_url = "https://s.staging.mmears.com"


def login():
    url = "https://s.staging.mmears.com/id/login/pwd"
    data = {
        "email": "bonny@mmears.com",
        "password": "mmears2016",
        "code": "123456"
    }
    s = r.post(url=url, data=data)


def addStandbyCount(dateConfig=str(int(time.mktime(datetime.date.today().timetuple()))*1000)):
    path = "/api/teacher/standby/addStandbyCount"
    url = base_url + path

    data = {
        "dateConfig": dateConfig,
        "configDetailes": json.dumps([{"courseTime": "09:00", "teacherNumber": 0}, {"courseTime": "09:30", "teacherNumber": 0},
                         {"courseTime": "10:00", "teacherNumber": 0}, {"courseTime": "10:30", "teacherNumber": 0},
                         {"courseTime": "11:00", "teacherNumber": 0}, {"courseTime": "14:00", "teacherNumber": 0},
                         {"courseTime": "14:30", "teacherNumber": 0}, {"courseTime": "15:00", "teacherNumber": 0},
                         {"courseTime": "15:30", "teacherNumber": 0}, {"courseTime": "16:00", "teacherNumber": 0},
                         {"courseTime": "16:30", "teacherNumber": 0}, {"courseTime": "17:00", "teacherNumber": 0},
                         {"courseTime": "17:30", "teacherNumber": 0}, {"courseTime": "18:00", "teacherNumber": 0},
                         {"courseTime": "18:30", "teacherNumber": 0}, {"courseTime": "19:00", "teacherNumber": 0},
                         {"courseTime": "19:30", "teacherNumber": 0}, {"courseTime": "20:00", "teacherNumber": 0},
                         {"courseTime": "20:30", "teacherNumber": 0}, {"courseTime": "21:00", "teacherNumber": 0}])
        }
    s = r.post(url=url, data=data)
    s = s.json()
    if s["code"]==400060003:
        print("已经配置stb")
def get_teacherName(teacherId):
    path = "/course/catalog/match/teacher/keyword?keyword={}".format(teacherId)
    url = base_url+path
    s = r.get(url=url)
    s = s.json()
    teacherName = s["result"][0]["name"]
    return teacherName
def standby_modify(teacherId,courseTime,dateConfig = str(int(time.mktime(datetime.date.today().timetuple()))*1000)):
    login()
    addStandbyCount(dateConfig)
    teacherName = get_teacherName(teacherId)
    path = "/api/teacher/standby/modify"
    url = base_url+path
    data = {
        "dateConfig": dateConfig,
        "configDetailes": json.dumps([{"teacherNumber": 100, "courseTime": courseTime, "teacherLists": [
            {"teacherId": teacherId, "teacherName": teacherName, "status": 0, "teacherClass": ""}],
                          "numEnough": False, "_change": True}])
    }
    s = r.post(url=url,data=data)
    print(s.json())
if __name__=="__main__":
    '''需要传入老师id跟stb课程时间点，默认创建的当日stb配置'''
    standby_modify("1223944","15:00")


