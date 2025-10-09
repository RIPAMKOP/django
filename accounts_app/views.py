from django.shortcuts import render,HttpResponse
# Create your views here.

def profile(request , username) :
    return HttpResponse(f'<h1> Hello {username} </h1>')
    


def info(request):
    return HttpResponse(f"This Is info page")