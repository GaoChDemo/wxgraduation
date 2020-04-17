from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    # return HttpResponse(u"欢迎光临!")
    return render(request, 'index.html')
