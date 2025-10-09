from django.shortcuts import render,HttpResponse


def profile(request , username) :
    return render(request , "accounts_app/profile.html")


def info(request):
    return HttpResponse(f"This Is info page")