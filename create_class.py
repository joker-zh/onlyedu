"""
coding: utf-8
@Time : 2021/9/14 13:11
@Author : zhanghang
@desc : 
@File : create_class.py
"""
import requests
import time
global token


# 登录后台管理员
def login():
    url = "http://octest.onlyeduschool.com:81/api/admin/login"
    data = {
        "password": "123456",
        "sid": 1,
        "username": "13122500673"
    }

    result = requests.post(url, json=data)
    globals()["token"] = result.json()["data"]["token"]


# 创建课节
def create_class():
    url = "http://octest.onlyeduschool.com:81/api/lesson/create"
    for i in range(0, 1):                # 配置课节数量
        body = {
            "beginTime": "2021-12-22 13:30:00",
            "controlMode": 1,
            "courseId": 606,
            "endTime": "2021-12-22 13:50:00",
            "introduction": "",
            "isPublic": 0,
            "members": [
                {
                    "role": "TEACHER",
                    "sysRole": 2,
                    "userId": 6105        # 配置老师
                },
                {
                    "role": "STUDENT",
                    "sysRole": 1,
                    "userId": 5975         # 配置学生
                }
            ],
            "name": "批量创建-"+str(i),
            "needRecord": 0,
            "onSale": 1,
            "recordMode": 1,
            "type": 1,
            "vidRes": "TRTCVideoResolution_640_360"
        }
        headers = {"token": token}
        r = requests.post(url, json=body, headers=headers)
        print(r.json())


if __name__ == '__main__':
    login()
    create_class()
