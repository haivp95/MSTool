import ldap
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.template import RequestContext
import requests

def LoginLDAP (request):
    username = ''
    password =''
    state = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = request.GET.get('username'), password = request.GET.get('password') )
        if user is not None:
            login(request, user)
            state = 'Welcome ' + username
        else:
            state = 'Not valid'
    return render(request, 'Login.html',{
        'state' : state, 'username' : username
    }
    )


