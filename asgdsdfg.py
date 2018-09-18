import requests
import re
from lxml import etree
import pymysql
import json
import time
    # print(x["saccountnum"])
url1="https://dp.nifa.org.cn/HomePage?method=getTargetOrgInfo&sorganation=91310115568071645J"
data=requests.get(url1).text
# print(data)
arr=[]
html = etree.HTML(data)
html_data = html.xpath('//div/div/div/table[@class="table right-table"]/tr/td')
for i in html_data:
    arr.append(i.text.replace("\r","").replace("\n","").replace("\t","").replace(" ",""))
# print(arr)
la=len(arr)
a=arr[0:32]
print(a)
index=arr.index('交易总额(万元)')
b = arr[32:index]
print(b)
lb = int(len(b) / 32)
print(lb)
c=arr[index+27:]
print(c)
lc=int(len(c)/27)
print(lc)

arr1=[]
p = re.compile(
    r'<td class="table-label"><i></i>(.*?)</td>',
    re.S | re.M)
q = re.findall(p, data)
for x in q:
    i=x.replace("\r","").replace("\n","").replace("\t","").replace(" ","")
    arr1.append(i)

p = re.compile(
    r'<!--<tr><td class="table-label">(.*?)</td>-->',
    re.S | re.M)
q = re.findall(p, data)
print(len(q))
if len(q)>1:
    biaoshi=q[1].replace("\r","").replace("\n","").replace("\t","").replace(" ","")
print(arr1)
print(arr1.index(biaoshi))

# tijiao=[]
for x in range(1,arr1.index(biaoshi)+1):
    tijiao = arr[32*x:32*(x+1)]
    tijiao.insert(0,arr1[x - 1])
    print(tijiao)
    tijiao=[]
