# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 11:33
# @Author  : lvzhimeng
# @FileName: get_course.py
# @Software: PyCharm
import requests
import json
d = []
d1 = []
def get_course():
    url = "https://s.mmears.com/api/teacher/course/all?_pn=1&_pi=50&sts=1619746200000&ets=1619746203000&_f_teacherId=&_f_flagSet&_f_status="
    headers = {

        "cookie":"_ga=GA1.2.504395125.1622430805; _gid=GA1.2.457062988.1622430805; staging_userId=839; mm_userId=11223; _fbp=fb.1.1622527520316.1673192537; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22839%22%2C%22%24device_id%22%3A%22179c569a8c5db2-0b92cbb67194c3-2363163-2073600-179c569a8c6a29%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22179c569a8c5db2-0b92cbb67194c3-2363163-2073600-179c569a8c6a29%22%7D; staging_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI4MzkiLCJuYW1lIjoiYm9ubnkiLCJzdXBwb3J0SWQiOm51bGwsImV4cCI6MTYyMjY4Njk3MywiaWF0IjoxNjIyNjAwNTczLCJlbWFpbCI6ImJvbm55QG1tZWFycy5jb20ifQ.t2HomBxnIkcDFD8itxJ2QTH2fPBZKy0doA1nJUAuq7UdfjgVPcvTj1I4W7-PQAddcTCxb-loteGd9top8w4w0w; _uetsid=64349f30c10b11eb9e61b5ca898eda95; _uetvid=d49f1bb09d0811ebb9a873401912c485; mmtoken=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMTIyMyIsIm5hbWUiOiLlkJXlv5fmoqYiLCJzdXBwb3J0SWQiOm51bGwsImV4cCI6MTYyMjY5ODc4MiwiaWF0IjoxNjIyNjEyMzgyLCJlbWFpbCI6InpoaW1lbmcubHZAaGFwcHktc2VlZC5jb20ifQ.S5QYLljWUXV_YKYmpU5m4Bw5ezJVaqqE6kP76pMoFhI_OZ655ecMO8CYMJ-XMX7jRWoDaXLo94vIQWAIrF6kFg; userId=2041; token=eREnlDgThBvgwBiA_v2d8c19VFONz5HXYXqH52ciI7R79U6JAN1JkKl-nA41tVAAwjXVAxFRlHQoRMEkJBQqF2Yt3n01hC--hGB7tbLL1tB8tJMy1dmi0vd9wOFRyrg2; ph=44bdef57; pm-Product=umfKDKz4yo43ctJB_rvJOfCV15AU6swqzKULlPSUjzGJ9SMK-4EajEZF6w48ArByWJshFjSs2Sgd9yOoe-9HVhQeWCe3emn46JvACJOTQORmvP3sP06rP8vf5hHCxZanZhuwGZ-b82uJMjHazhT2f3nujG1EOo4yB5wb04t3X6tXqZV6kalSnwxQBRqkJ0pMUe42VXwDc7K5njYNMmf-u0A-xPPWNMTVo9kfZT0XQlLPEo8yKDqPpUsoFA4IZp-_hXxbaZ_muLH3bZk1djtYvg; SERVERID=44d522618aa28320574b919c3f8435e0|1622614653|1622614116"
    }

    s = requests.get(url=url,headers=headers,verify=False)
    s = s.json()

    for i in s["result"]["data"]:
        id = i["teacherId"]
        d.append(id)
    print(d)
def get_succes():

    url1 = "https://api.mmears.com/teacher/pay/course/query"
    headers1 = {
        "Content-Type":"application/json; charset=UTF-8",
        "X-Auth-Token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMTIyMyIsIm5hbWUiOiLlkJXlv5fmoqYiLCJzdXBwb3J0SWQiOm51bGwsImV4cCI6MTYyMjY5ODc4MiwiaWF0IjoxNjIyNjEyMzgyLCJlbWFpbCI6InpoaW1lbmcubHZAaGFwcHktc2VlZC5jb20ifQ.S5QYLljWUXV_YKYmpU5m4Bw5ezJVaqqE6kP76pMoFhI_OZ655ecMO8CYMJ-XMX7jRWoDaXLo94vIQWAIrF6kFg",
        "X-App-Id":"6"
    }
    data1 = {
        "minStartTime":1619712000000,
        "maxStartTime":1619798399000,
        "courseSubTimeList":["09:30"],

        "pageIndex":1,
        "pageSize":100
    }
    data1 = json.dumps(data1)
    s = requests.post(url=url1,data=data1,headers=headers1)
    s = s.json()
    print(s)
    for i in s["data"]["records"]:
        id = i["teacherId"]
        d1.append(id)
    print(d1)
get_course()
get_succes()
print("老系统数据条数%s"%len(d))
print("新系统数据条数%s"%len(d1))
for i in d1:
    if i in d:
        pass
    else:
        print(i)