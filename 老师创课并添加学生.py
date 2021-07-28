import requests
import json
import time
'''
需要创课老师账号、密码及约课学生手机号，默认选当日最近可创课程，学生约课约最新创建的课
'''


headers1 = {
    "content-type":"application/json; charset=UTF-8",

}
headers2 = {
    "x-app-id":"6",
    # "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "content-type": "application/json; charset=UTF-8",
}
base_url1 = "https://tapi-staging.mmears.com"
base_url2 = "https://apistaging.mmears.com"
def teacher_login(teacher_email,password):
    path = "/t/tn/user/foreign/login"
    url = base_url1+path
    data ={
        "callback": "http://t.staging.mmears.com",
        "email": teacher_email,
        "password": password
    }
    s = requests.post(url,data=data)
    s = s.json()
    token = s["data"]["serviceTokenCookie"]["value"]
    headers1["x-user-token"]=token
    print(headers1)
def courseType(teacher_email, password):
    teacher_login(teacher_email, password)
    a = time.time()
    b = time.localtime(a)
    c = time.strftime("%Y-%m-%d", b)
    d = time.mktime(time.strptime(c, "%Y-%m-%d"))
    d = int(d * 1000)
    path = "/t/tc/book/all/units?courseType=MAIN&weekStartTime={0}".format(d)
    url = base_url1+path
    data = {
        "courseType": "MAIN",
        "weekStartTime": d
    }
    # data = json.dumps(data)
    s = requests.get(url=url,data=data,headers=headers1)
    s = s.json()
    class_list = s["data"]
    print(class_list)
    for i in class_list:
        if i["status"]=="AVAILABLE":
            startTime = i["startTime"]
            select_class(startTime)
            break
        elif i["status"]=="STANDBY_AVAILABLE":
            startTime = i["startTime"]
            select_class_standby(startTime)
            break


def select_class(startTime):
    path = "/t/tc/book/batch"
    url = base_url1+path
    data = {
        "courseType": "MAIN",
        "startTimes": [startTime]
    }
    data = json.dumps(data)
    s = requests.post(url=url,data=data,headers=headers1)
    s = s.json()
    if s["code"]=="BIZ_TEACHER_BOOK_COURSE_WITHIN_10_MINUTE":
        startTime = str(int(startTime)+1800000)
        data = {
            "courseType": "MAIN",
            "startTimes": [startTime]
        }
        data = json.dumps(data)
        s = requests.post(url=url, data=data, headers=headers1)
        s = s.json()

    print(s)
def select_class_standby(startTime):
    path = "/t/tc/book/standby"
    url = base_url1+path
    data = {
        "startTime": startTime
    }
    data = json.dumps(data)
    s = requests.post(url=url,data=data,headers=headers1)
    print(s.json())
def cc_login():
    path = "/auth/login"
    url = base_url2+path
    data = {
        "code": "123456",
        "email": "bonny@mmears.com",
        "password": "bW1lYXJzMjAxNg=="
    }
    s = requests.post(url=url,data=data)
    token = s.json()["data"]["token"]
    headers2["x-auth-token"]=token

def get_teacherId(teacher_email):
    path = "/teacher/apply/get/teacher/info"
    url = base_url2+path
    p = {
        "searchContent": teacher_email
    }
    s = requests.get(url=url,params=p,headers=headers2)
    s = s.json()
    teacherId=s["data"][0]["teacherId"]
    return teacherId
def get_studentId(student_phone):
    cc_login()
    path = "/teacher/course/operate/match/student/keyword"
    url = base_url2+path
    p = {
        "keyword": student_phone
    }
    s = requests.get(url=url, params=p, headers=headers2)
    s = s.json()
    studentId = s["data"][0]["studentId"]
    print(studentId)
    return studentId
def get_teacher_course(teacherId):
    path = "/teacher/course/operate/list"
    url = base_url2+path
    a = time.time()
    b = time.localtime(a)
    c = time.strftime("%Y-%m-%d", b)
    data = {
        "courseEndTime": c,
        "courseStartTime": c,
        "pageIndex": 1,
        "pageSize": 100,
        "teacherId": teacherId,
    }
    data = json.dumps(data)
    s = requests.post(url=url,data=data,headers=headers2)
    s = s.json()
    print(s)
    # courseId = s["data"]["records"][-1]["courseId"]
    startTime = s["data"]["records"][-1]["startTime"]

    return startTime

def add_student(teacher_email,student_phone):
    cc_login()
    studentId = get_studentId(student_phone)
    teacherId = get_teacherId(teacher_email)
    startTime = get_teacher_course(teacherId)


    path = "/teacher/course/operate/add"
    url = base_url2+path
    headers2["content-type"]="application/x-www-form-urlencoded; charset=UTF-8"
    data = {
        "startTime":startTime ,
        "courseType": 0,
        "lesson": 1,
        "unit": 2,
        "level": 2,
        "studentId": studentId,
        "teacherId": teacherId
    }
    # data = json.dumps(data)
    s = requests.post(url=url,data=data,headers=headers2)
    print(s.json())
teacher_email='1099182107@qq.com'
password = '1234qwer'
student_phone = '13247705056'
courseType(teacher_email,password)         #老师创课
# add_student(teacher_email,student_phone)   #学生约课
