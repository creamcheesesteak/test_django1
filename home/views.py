from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request


def index(request):
    path = request.path
    resultstr = ''
    if path == '/home':
        resultstr = '<h1>여기는 home입니다</h1>'
    else :
        resultstr = '<h1>여기는 [임태혁]입니다</h1>'
    return HttpResponse(resultstr)

def index01(request):
    result = {'first':'taehyeok','second':'im'}
    return render(request,'index.html',context=result)

def index02(ruquest):
    # request.GET['']
    result = {'first':request.GET['taehyeok'], 'second':request.GET['im']}
    return render(request, 'index.html', context=result)

