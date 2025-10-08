from django.shortcuts import render,HttpResponse
# Create your views here.
users = ['amir', 'milad' , 'hoseein' , 'ali', 'farid', 'reza']
blocked_users = ['milad','ali']


def profile(request , username):
    if username in users: 
             if username in blocked_users: 
                 return HttpResponse(f'<h1> {username} is blocked <h1>')
             else:
                     return HttpResponse(f"<h1 style='color:red'> This Is {username} profile <h1>")
    else:       
                   return HttpResponse('This Username is not registered')


def info(request):
    return HttpResponse(f"This Is info page")