from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "home_app/home.html")



def contactus(request):
    return HttpResponse('Hi This is contact us page')