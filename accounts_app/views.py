from django.shortcuts import render,HttpResponse
# Create your views here.


def profile(request , username):
    return HttpResponse(f"This Is {username} profile")



def info(request):
    return HttpResponse(f"This Is info page")