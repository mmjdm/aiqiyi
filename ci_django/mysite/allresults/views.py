from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os
import time


def allresults(request):
    dirname = request.POST['dirname']
    if os.path.exists(os.getcwd() + os.sep + "allresults.txt"):
        f = open(os.getcwd() + os.sep + "allresults.txt", 'a+')
        # f.write(dirname +str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+ '\n')
        f.close()
    else:
        f = open(os.getcwd() + os.sep + "allresults.txt", 'w')
        f.write(dirname + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'\n')
        f.close()
    # print(dirname)
    return HttpResponse("Hello, world! hahahahaha!")
