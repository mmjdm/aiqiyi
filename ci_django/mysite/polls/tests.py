from django.test import TestCase

# Create your tests here.
import requests
import os
file = {'myfile': open('/Users/ranli/01.png','rb')}
data = {
    'dirname': '【分钟级】【基础准入】【trunk】-865304041852401-HUAWEI-SNE-AL00-8.1.0',
}
r = requests.post('http://10.3.4.51:8000/polls/', files=file, data=data)
#print(r.text)
print(os.path.dirname('/Users/ranli/PycharmProjects/ci_django/mysite/trunk/865304041852401-HUAWEI-SNE-AL00-8.1.0'))
di ='/Users/ranli/PycharmProjects/ci_django/mysite/trunk/865304041852401-HUAWEI-SNE-AL00-8.1.0'
# if not os.path.exists(os.path.dirname(di)):
#     os.mkdir(os.path.dirname(di))
# if not os.path.exists(di):
#     os.mkdir(di)