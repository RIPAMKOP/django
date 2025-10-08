from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Hi This is home page')



def contactus(request):
    return HttpResponse('Hi This is contact us page')