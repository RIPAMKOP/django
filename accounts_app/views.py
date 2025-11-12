from django.shortcuts import render, HttpResponse
from django.http import Http404

users = [
    {
        'username': 'amir',
        'name': 'amirhossein',
        'lastname': 'amiri',
        'phone': '09368432094',
        'city': 'iran',
    },
    {
        'username': 'milad',
        'name': 'milad',
        'lastname': 'dehyami',
        'phone': '09368432094',
        'city': 'esf',
    },
    {
        'username': 'hossein',
        'name': 'hossein',
        'lastname': 'rasti',
        'phone': '09368432094',
        'city': 'ysj',
    }
]

def userslist(request):
    # user_list = users
    return render(request, 'accounts_app/users_list.html' , context= {'user_list': users})
    
def profile(request, username):
    for user in users:
        if user['username'] == username:
            return render(request, 'accounts_app/profile.html', context={'user': user})
    raise Http404('This user does not exist')


def info(request):
    return render(request, "accounts_app/info.html")
