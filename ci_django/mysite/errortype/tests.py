from django.test import TestCase

# Create your tests here.
import requests
import os
for root, dirs, files in os.walk("/Users/ranli/PycharmProjects/ci_django/mysite/AssertionFailedError/ 1571eab2-AssertionFailedError", topdown=False):
    for i in files:
        ff = open(root+os.sep+i,'r').readlines()
        for ii in ff:
            if 'the normal log is： am instrument ' in ii:
                print(ii.replace('\n',''))
                break
# file = {'myfile': open('/Users/ranli/01.png','rb')}
# data = {
#     'dirname': '865304041852401-HUAWEI-SNE-AL00-8.1.0',
# }
# r = requests.post('http://10.3.4.51:8000/errortype/', files=file, data=data)
# print(r.text)
# print(os.path.dirname('/Users/ranli/PycharmProjects/ci_django/mysite/trunk/865304041852401-HUAWEI-SNE-AL00-8.1.0'))
# di ='/Users/ranli/PycharmProjects/ci_django/mysite/trunk/865304041852401-HUAWEI-SNE-AL00-8.1.0'
