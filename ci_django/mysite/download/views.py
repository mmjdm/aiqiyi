from django.shortcuts import render
from django.http import FileResponse
# Create your views here.
import os
dirnamedic = {
    '【分钟级】【基础准入】【trunk】': 'trunk',
    '【分钟级】【基础准入】【tag】': 'tag',
    '【分钟级】【4系统】【trunk】': '4trunk',
    '【分钟级】【5系统】【trunk】': '5trunk',
    '【分钟级】【6系统】【trunk】': '6trunk',
    '【分钟级】【7系统】【trunk】': '7trunk',
    '【分钟级】【9系统】【trunk】': '9trunk',
    '【小时级】【BAT】': 'BAT',
}


def download(request):
    dirname = request.GET.get('dirname')
    filename = request.GET.get('filename')
    if '分钟级' in dirname:
        dirname = dirnamedic[dirname.split('-')[0]] + os.sep + dirname.replace(dirname.split('-')[0]+'-', '')
    else:
        dirname = dirname.split('-')[0] + os.sep + dirname.replace(dirname.split('-')[0]+'-', '')
    file = open(os.getcwd() + os.sep + dirname + '/' + filename, 'rb')
    response = FileResponse(file)
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    if os.path.exists(os.getcwd() + os.sep + "记录下载次数.txt"):
        f = open(os.getcwd() + os.sep + "记录下载次数.txt", 'a+')
        linenum = len(f.readlines()) + 1
        f.write(str(linenum)+':'+ip + '\n')
        f.close()
    else:
        f = open(os.getcwd() + os.sep + "记录下载次数.txt", 'w')
        f.write('1:'+ ip + '\n')
        f.close()
    # response['Content-Type'] = 'application/vnd.android.package-archive'
    response['Content-Disposition'] = 'attachment;filename='+filename
    return response

