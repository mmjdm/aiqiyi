from django.test import TestCase

# Create your tests here.
import requests
from contextlib import closing

url = "http://10.3.4.51:8000/download?"
payload = 'dirname=trunk-865304041852401-HUAWEI-SNE-AL00-8.1.0&filename=iQiYi_Video_10.5.5_20190509_114902.apk'
import requests
print(url+payload)
print("【分钟级】【基础准入】【trunk】-865304041852401-HUAWEI-SNE-AL00-8.1.0".split('-'))
herder = {
            "Content-Type": "application/vnd.android.package-archive",
          }

# r = requests.get(url, headers=herder, params=payload)
#
# # open打开excel文件，报存为后缀为xls的文件
# fp = open("yoyo.apk", "wb")
# fp.write(r.content)
# fp.close()
import os

# if os.path.exists(os.getcwd() + os.sep + "记录下载次数.txt"):
#     f = open(os.getcwd() + os.sep + "记录下载次数.txt", 'r+')
#     aa = len(f.readlines())+1
#     f.write(str(aa)+'\n')
#     f.close()
# else:
#     f = open(os.getcwd() + os.sep + "记录下载次数.txt", 'w')
#     f.write('1'+'\n')
#     f.close()
f = open('/Users/ranli/20190510161214_844827_10.log','r').readlines()
for i in f:
    if 'zip' in i:
        print(i)

