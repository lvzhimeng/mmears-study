# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 11:19
# @Author  : lvzhimeng
# @FileName: test.py
# @Software: PyCharm
import urllib3
import json
from locust import HttpUser, task, TaskSet
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class MyTest(TaskSet):
    def on_start(self):   #在任务开始时只执行一次该动作
        pass
    @task(2)
    def get_blog(self):
        # 定义请求头
        header = {
                "x-auth-token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI4MzkiLCJuYW1lIjoiYm9ubnkiLCJzdXBwb3J0SWQiOm51bGwsImV4cCI6MTYyNTcxMTMzOCwiaWF0IjoxNjI1NjI0OTM4LCJlbWFpbCI6ImJvbm55QG1tZWFycy5jb20ifQ.Dw6F2r6nJvDvKia0vl5ylb4Oz9FqE4YNGew2uANRrQ6SBMsnTo1ga6NX0tY3h3W_mzPc-uzXy528sE5Vyrtr9g",
                "x-app-id":"6",
                "content-type":"application/json; charset=UTF-8"
            }
        data = {
            "courseEndTime": "2021-07-08",
            "courseStartTime": "2021-07-08",
            "fixedClass": "true",
            "pageIndex": 1,
            "pageSize": 100,
            "teacherId": 1235614
        }
        data= json.dumps(data)
        with self.client.post("/teacher/course/operate/list", headers=header, data=data ,verify=False, catch_response=True) as response:
            print(response.text)
            if response.status_code == 200:
                if response.json()['code'] == "OK":
                    response.success()
                    print("success")
                else:
                    response.failure('Failed!')
                    print("程序状态码非OK，fails")
            else:
                response.failure('Failed!')
                print("网络状态码非200，fails")



class websitUser(HttpUser):
    tasks = [MyTest]     #指向一个TaskSet类，此属性必填
    min_wait = 3000  # 单位为毫秒，每个用户执行两个任务间隔时间的上下限，不指定默认1s
    max_wait = 6000  # 单位为毫秒
    host = ''    #此处设置host在运行的时候或跑脚本的时候设置host会覆盖


if __name__ == "__main__":
    import os
    os.system("locust -f test.py --host=https://apistaging.mmears.com --web-host=127.0.0.1")