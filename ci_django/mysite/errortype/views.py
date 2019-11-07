from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import os


def uploaderrortype(request):
    File = request.FILES.get("myfile", None)
    if File is None:
        a = '请选择上传文件!'
        return render(request, 'upload/fp.html', locals())
    else:
        dirname = request.POST['dirname']
        if not os.path.exists(os.path.dirname(os.getcwd() + os.sep + dirname.split('-')[1])):
            newdir = os.path.dirname(os.getcwd() + os.sep + dirname.split('-')[1])
            os.mkdir(newdir)

        lujing = "./"+dirname.split('-')[1]+'/' + "%s" % str(dirname) + "/" + "%s" % File.name
        with open(lujing, 'wb+') as f:
            for chunk in File.chunks():
                f.write(chunk)
        a = '上传成功!!'
    return HttpResponse("Hello, world! hahahahaha!")
