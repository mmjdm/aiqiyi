from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
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


def upload(request):
    File = request.FILES.get("myfile", None)
    if File is None:
        a = '请选择上传文件!'
        return render(request, 'upload/fp.html', locals())
    else:
        dirname = request.POST['dirname']
        dirname = dirnamedic[dirname.split('-')[0]] + os.sep + dirname.replace(dirname.split('-')[0]+'-', '')
        if not os.path.exists(os.path.dirname(os.getcwd() + os.sep + dirname)):
            newdir = os.path.dirname(os.getcwd() + os.sep + dirname)
            os.mkdir(newdir)
        if not os.path.exists(os.getcwd() + os.sep + dirname):
            os.mkdir(os.getcwd() + os.sep + dirname)
        lujing = "./" + "%s" % str(dirname) + "/" + "%s" % File.name
        for root, dirs, files in os.walk("./" + "%s" % str(dirname)):
            for name in files:
                print(os.path.join(root, name))
                try:
                    print(File.name.split('_')[2])
                    if File.name.split('_')[2] not in name:
                        os.remove(os.path.join(root, name))
                except:
                    pass
        with open(lujing, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
    return HttpResponse("Hello, world! hahahahaha!")


