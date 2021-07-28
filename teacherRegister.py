import requests
from get_email import get_email
def teacher_Register():
    try:
        email = get_email()
        url = "https://tapi-staging.mmears.com/t/tn/user/register"
        headers = {
            "content-type":"application/x-www-form-urlencoded;charset=UTF-8"
        }
        data = {
            "captcha":'test20210205',
            "email": email,
            "password": "1234qwer",
            "poster":"",
            "referralCode":"1223944",
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
if __name__=="__main__":
    teacher_Register()