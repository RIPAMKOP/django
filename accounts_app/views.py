from django.shortcuts import render,HttpResponse
from django.http import Http404

users = [
    {
        'username' : 'amir' , 
        'name' : 'amirhossein', 
        'lastname' : 'amir' , 
        'phone' : '09368432094' ,
        'city' : 'iran'
    },
    {
        'username' : 'milad80' , 
        'name' : 'milad', 
        'lastname' : 'dehyami' , 
        'phone' : '09368432094' ,
        'city' : 'esf'
    },
    {
        'username' : 'hossein90' , 
        'name' : 'hossein', 
        'lastname' : 'rasti' , 
        'phone' : '09368432094' ,
        'city' : 'ysj'
    },
]

def profile(request , username) :
    for user in users : 
        if user['username'] == username:
            return render(request, 'accounts_app/profile.html', context={'user': user})
        
        return Http404('This user in not exist')
   


def info(request):
    return render(request , "accounts_app/info .html")