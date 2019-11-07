from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os
import time
dirnamedic = {
    '【分钟级】【基础准入】【trunk】': 'trunk',
    '【分钟级】【基础准入】【tag】': 'tag',
    '【分钟级】【4系统】【trunk】': '4trunk',
    '【分钟级】【5系统】【trunk】': '5trunk',
    '【分钟级】【6系统】【trunk】': '6trunk',
    '【分钟级】【7系统】【trunk】': '7trunk',
    '【分钟级】【9系统】【trunk】': '9trunk',
}


def timelog(request):
    dirname = request.POST['dirname']
    dirpath = os.getcwd() + os.sep + 'timelogresults'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    dirpath = os.getcwd() + os.sep + 'timelogresults' + os.sep + dirnamedic[dirname.split('-')[0]]
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    today = time.strftime("%Y-%m-%d", time.localtime()).replace('-','')
    dirpath = os.getcwd() + os.sep + 'timelogresults' + os.sep + dirnamedic[dirname.split('-')[0]]+os.sep+today+'.html'
    if not os.path.exists(dirpath):
        f = open(dirpath, 'w')
        for i in open(os.getcwd() + os.sep+'test.html').readlines():
            f.write(i)
        f.close()
    timelog = request.POST['timelog'].split('-')
    new_taday_timelog_html = ''
    for i in open(dirpath,'r').readlines():
        if 'runner执行总时长数据' in i:
            i = i.split(']')[0]+timelog[0]+','+']'+i.split(']')[1]
        if 'runner初始化时长数据' in i:
            i = i.split(']')[0]+timelog[1]+','+']'+i.split(']')[1]
        if 'runner安装apk时长数据' in i:
            i = i.split(']')[0]+timelog[2]+','+']'+i.split(']')[1]
        if '冒烟用例1执行时长数据' in i:
            i = i.split(']')[0]+timelog[3]+','+']'+i.split(']')[1]
        if '冒烟用例2执行时长数据' in i:
            i = i.split(']')[0]+timelog[4]+','+']'+i.split(']')[1]
        if '冒烟用例3执行时长数据' in i:
            i = i.split(']')[0]+timelog[5]+','+']'+i.split(']')[1]
        if '冒烟用例4执行时长数据' in i:
            i = i.split(']')[0]+timelog[6]+','+']'+i.split(']')[1]
        if '冒烟用例5执行时长数据' in i:
            i = i.split(']')[0]+timelog[7]+','+']'+i.split(']')[1]
        new_taday_timelog_html += i
    f = open(dirpath, 'w')
    f.write(new_taday_timelog_html)
    f.close()
    print(dirname)
    print(timelog)
    return HttpResponse("Hello, world! hahahahaha!")
