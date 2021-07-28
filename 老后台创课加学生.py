import requests
import time
import math
r = requests.session()
def get_time():
    t = math.floor((int(time.time())+300)/300)*300000
    print(t)
    return t

def login():
    url = "https://s.staging.mmears.com/id/login/pwd"
    data = {
        "email": "bonny@mmears.com",
        "password": "mmears2016",
        "code": "123456"
    }
    s = r.post(url=url, data=data)

    print(s.json())
def get_teacherId():
    login()
    url = "https://s.staging.mmears.com/user/search?user=1099182107%40qq.com"
    s = r.get(url=url)
    print(s.json())
def open_class(teacherId="1223944",studenPhone="13247705056",t=get_time(),level=2,unit=2,lesson=1):
    login()
    url = "https://s.staging.mmears.com/api/client/course/open"
    data = {
        "teacherId": teacherId,
        "startTime": t,
        "classType": 0
    }
    s = r.post(url=url,data=data)
    print(s.json())
    add_student(teacherId,t,studenPhone,level,unit,lesson)
def get_studentId(studentPhone):
    url = "https://s.staging.mmears.com/course/catalog/match/student/keyword?keyword={0}".format(studentPhone)
    s = r.get(url=url)
    s = s.json()
    studentId = s["result"][0]["studentId"]
    return studentId
def add_student(teacherId,t,studenPhone,level,unit,lesson): #level:1-7,unit:1-12,lesson:1-8
    studentId = get_studentId(studenPhone)
    url = 'https://s.staging.mmears.com/api/client/course/add'
    data = {
        "teacherId": teacherId,
        "startTime": t,
        "studentId": studentId,
        "level": level,
        "unit": unit,
        "lesson": lesson,
        "classType": "0"
    }
    s = r.post(url=url,data=data)
    print(s.json())
# open_class(teacherId='1223944',studenPhone='13247705056')
# open_class(teacherId="1223944",studenPhone="13247705056",level="70001",unit="1",lesson="2")
# get_time()
login()