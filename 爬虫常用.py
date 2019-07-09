import requests
import time
import json
import base64
import hashlib
import re
import datetime

headers=''
headers = headers.strip().split('\n')
headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}

data=''
p = re.compile(
    r'>(.*?)<',
    re.S | re.M)
q = re.findall(p, data)

#剔除标签
import re
html='<a href="//www.jb51.net">脚本之家</a>,Python学习！'
dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',html)
print(dd)

def clean(data):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', data).replace('\n','').replace('\t','').replace('\r','').replace('&nbsp;','').strip()
    return dd

a='7天前'
print(a[1:3]=='天前')
print(int(time.time())-int(a[0])*24*3600)
timeArray=time.localtime(int(time.time())-int(a[0])*24*3600)
otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
print(otherStyleTime.split('-')[0]+'年'+otherStyleTime.split('-')[1]+'月'+otherStyleTime.split('-')[2]+'日')

#忽略证书之后忽略警告用
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#读excel
import xlrd
data = xlrd.open_workbook('')
table = data.sheets()[0]
a= table.col_values(0)

#时间处理

#日期转时间戳
data1='2018-08-07 16:57:22'
#转struct_time
date=time.strptime(data1,'%Y-%m-%d %H:%M:%S')
print(date)
timeStamp=int(time.mktime(date))
print(timeStamp)
#上个月第一天
fist = datetime.date(datetime.date.today().year,datetime.date.today().month-1,1)
print(fist)
#上个月最后一天
last = datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)
print(last)

time1=int(time.time())
localtime=time.localtime(time1)
print(localtime)
print(localtime.tm_year)

date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time1))
print(date)

#返回日期之前n天的日期列表
def get_nday_list(date,n):
    before_n_days = []
    t = time.strptime(date, "%Y-%m-%d")
    y, m, d = t[0:3]
    for i in range(1, n + 1)[::-1]:
        before_n_days.append(str(datetime.datetime(y, m, d) - datetime.timedelta(days=i)).split(' ')[0])
    return before_n_days

#时间戳转日期
def timeStamp(timeNum):
    timeStamp = float(timeNum) / 1000
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    return otherStyleTime

#代理ip
def proxies():
    ipdata = requests.get(
        'http://api.ip.data5u.com/dynamic/get.html?order=62d0ea767e6a053795e7df2c8946483a&json=1&sep=3').text
    ipdata = json.loads(ipdata)
    print(ipdata)
    for x in ipdata['data']:
        ip = str(x['ip']) + ':' + str(x['port'])
        proxies = {'http': ip, 'https': ip}
    return proxies

# user_agent_list
import random
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
headers["User-Agent"] = random.choice(user_agent_list)

# s='VNw==zNzblltbGtRWE56WlhSVWNtRnVjMGxrSnpvd0xDZGlhV1JKWkNjNk16UTROemdzSjJsa0p6b3hOakExTURNNExDZHBiblpsYzNSTmIyNWxlU2M2TlRBd01EQXVNQ3duYVhOemRXbHVaMVJwYldVbk9pY3lNREUzTFRBeExUQTBKeXduY0dodmJtVW5PaWN4TXpncUtpb3FOekl4T1Njc0ozSmxjMlZ5ZG1WSlpDYzZNQ3duZEdsdFpTYzZKekl3TVRjdE1ERXRNRFFnTVRNNk5UVTZNRGduZlN4N0oySnBaRUZ6YzJWMFZISmhibk5KWkNjNk1Dd25ZbWxrU1dRbk9qTTBPRGM0TENkcFpDYzZNVFl3TlRBek5pd25hVzUyWlhOMFRXOXVaWGtuT2pNd01EQXdMakFzSjJsemMzVnBibWRVYVcxbEp6b25NakF4Tnkwd01TMHdOQ2NzSjNCb2IyNWxKem9uTVRNM0tpb3FLakF5TlRnbkxDZHlaWE5sY25abFNXUW5PakFzSjNScGJXVW5PaWN5TURFM0xUQXhMVEEwSURFek9qVTFPakF5SjMwc2V5ZGlhV1JCYzNObGRGUnlZVzV6U1dRbk9qQXNKMkpwWkVsa0p6b3pORGczT0N3bmFXUW5PakUyTURVd016VXNKMmx1ZG1WemRFMXZibVY1SnpveE5UQXdNQzR3TENkcGMzTjFhVzVuVkdsdFpTYzZKekl3TVRjdE1ERXRNRFFuTENkd2FHOXVaU2M2SnpFNE5pb3FLaW93TmprMkp5d25jbVZ6WlhKMlpVbGtKem93TENkMGFXMWxKem9uTWpBeE55MHdNUzB3TkNBeE16bzFOVG93TWlkOUxIc25ZbWxrUVhOelpYUlVjbUZ1YzBsa0p6b3dMQ2RpYVdSSlpDYzZNelE0Tnpnc0oybGtKem94TmpBMU1ETTBMQ2RwYm5abGMzUk5iMjVsZVNjNk5UQXdNQzR3TENkcGMzTjFhVzVuVkdsdFpTYzZKekl3TVRjdE1ERXRNRFFuTENkd2FHOXVaU2M2SnpFek5Db3FLaW93TWpVM0p5d25jbVZ6WlhKMlpVbGtKem93TENkMGFXMWxKem9uTWpBeE55MHdNUzB3TkNBeE16bzFOVG93TUNkOUxIc25ZbWxrUVhOelpYUlVjbUZ1YzBsa0p6b3dMQ2RpYVdSSlpDYzZNelE0Tnpnc0oybGtKem94TmpBMU1ETXpMQ2RwYm5abGMzUk5iMjVsZVNjNk5EQXdNREF1TUN3bmFYTnpkV2x1WjFScGJXVW5PaWN5TURFM0xUQXhMVEEwSnl3bmNHaHZibVVuT2ljeE16VXFLaW9xTWprM05pY3NKM0psYzJWeWRtVkpaQ2M2TUN3bmRHbHRaU2M2SnpJd01UY3RNREV0TURRZ01UTTZOVFU2TURBbmZTeDdKMkpwWkVGemMyVjBWSEpoYm5OSlpDYzZNQ3duWW1sa1NXUW5Pak0wT0RjNExDZHBaQ2M2TVRZd05UQXpNaXduYVc1MlpYTjBUVzl1Wlhrbk9qSXdNREF3TGpBc0oybHpjM1ZwYm1kVWFXMWxKem9uTWpBeE55MHdNUzB3TkNjc0ozQm9iMjVsSnpvbk1UTTRLaW9xS2pnM01qZ25MQ2R5WlhObGNuWmxTV1FuT2pBc0ozUnBiV1VuT2ljeU1ERTNMVEF4TFRBMElERXpPalUxT2pBd0ozMHNleWRpYVdSQmMzTmxkRlJ5WVc1elNXUW5PakFzSjJKcFpFbGtKem96TkRnM09Dd25hV1FuT2pFMk1EVXdNekVzSjJsdWRtVnpkRTF2Ym1WNUp6bzBNREF3TUM0d0xDZHBjM04xYVc1blZHbHRaU2M2SnpJd01UY3RNREV0TURRbkxDZHdhRzl1WlNjNkp6RTFNaW9xS2lvd016VTFKeXduY21WelpYSjJaVWxrSnpvd0xDZDBhVzFsSnpvbk1qQXhOeTB3TVMwd05DQXhNem8xTlRvd01DZDlYUT0Nw==9'
# s=bytes(s,encoding = "utf8")
# decode = base64.b64decode(s.decode('utf-8'))
# print(decode)
# print(bytes.decode(decode)  )
#
# a='borrow_tender_content_tabs_v2_gou_record&is_full=1&borrow_account_scale=100.00&borrow_nid=20170900480&tender_times=45&borrow_account_yes=1000000.00&full_proportion=0.20'
# print(a)
# encodestr=base64.b64encode(a.encode('utf-8'))
# print(encodestr)
# encodestr=bytes.decode(encodestr)
# print(encodestr)