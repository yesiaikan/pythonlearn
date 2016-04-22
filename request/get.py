import httplib
import requests
#encoding=utf-8

__author__ = 'muli'

# conn = httplib.HTTPConnection("sandbox.sjws.baidu.com", 8080)
# conn.request("GET", "/dianhua_api/3.0/report/query?tel=10086")
# res = conn.getresponse()
# print res.status
# print res.reason
# print res.read()


r = requests.get("http://sandbox.sjws.baidu.com:8080/dianhua_api/3.0/report/query?tel=10086", timeout=1)
print r
print r.encoding
print r.headers
print r.text
# print r.cookies

r.raise_for_status()