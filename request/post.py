import httplib
import requests
import json

__author__ = 'muli'

conn = httplib.HTTPConnection("127.0.0.1", 8889)

url = "/dianhua_api/5.0/report/query?auth_ver=2&appkey=50b13132bb394901f151bc12&nonce=1429187945710&model=HTC+Sensation+XE+with+Beats+Audio+Z715e&is=460010400509006&signmd5=2209274221&op=46001&vendor=HTC&locale=zh_CN&pkg=com.baidu.query.sample&tk=BmS5eqGsIdk%2Fv7h3Fn0i4w%3D%3D&h=960&vn=1.0&w=540&v=1&ntt=HSDPA&ie=359614041402061&sdk=15&dpi=240&sdk_api=5&sdk_ver=1.4.0&checkStr=f58c39781d5adfe6604f35a5a91e3743&s=ae3f7dfa8c53cd16207fd0b29273600c"

msg="jj85aFbZW2CKF3oZPygx8S1YPTm0GnFvjR6E2w7f+WnOJBycS8o0vpqiK4nGfZCPU2eD\/cuAo76S\n3yjBa7mG9m0kjnKDiOHoP8AOOFb5lcQl7uh36hiB\/imw5SFbM\/bDdLgFho1VZbUT043JR5iMu3I7\nW+yT5v\/gARrcf8MxQ\/fRmk6RM8kT2dzeay6yaF\/F73Qs1JTg3NWDk9wwpd2O5A==\n"

body = {"msg":"jj85aFbZW2CKF3oZPygx8S1YPTm0GnFvjR6E2w7f+WnOJBycS8o0vpqiK4nGfZCPU2eD\/cuAo76S\n3yjBa7mG9m0kjnKDiOHoP8AOOFb5lcQl7uh36hiB\/imw5SFbM\/bDdLgFho1VZbUT043JR5iMu3I7\nW+yT5v\/gARrcf8MxQ\/fRmk6RM8kT2dzeay6yaF\/F73Qs1JTg3NWDk9wwpd2O5A==\n","createTime":1429187945668}

print json.dumps(body, ensure_ascii=True)

# data = json.JSONEncoder().encode(body)

headers = {"Content-type": "application/x-www-from-urlencoded", "Accept":"text/plain"}

# conn.request("POST", url, data, headers)
# resp = conn.getresponse()
# print resp.status
# print resp.reason
# print resp.read()


print '--------------------'

u = 'http://sandbox.sjws.baidu.com:8080/dianhua_api/5.0/report/query?auth_ver=2&appkey=50b13132bb394901f151bc12&nonce=1429187945710&model=HTC+Sensation+XE+with+Beats+Audio+Z715e&is=460010400509006&signmd5=2209274221&op=46001&vendor=HTC&locale=zh_CN&pkg=com.baidu.query.sample&tk=BmS5eqGsIdk%2Fv7h3Fn0i4w%3D%3D&h=960&vn=1.0&w=540&v=1&ntt=HSDPA&ie=359614041402061&sdk=15&dpi=240&sdk_api=5&sdk_ver=1.4.0&checkStr=f58c39781d5adfe6604f35a5a91e3743&s=ae3f7dfa8c53cd16207fd0b29273600c'

r = requests.post(u, data=json.dumps(body))

print r.text