import requests
#申请临时邮箱
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
if __name__=="__main__":
    print(get_email())