import ldap
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth import login, authenticate
import django.contrib.auth
from django.template import RequestContext
import requests


ldap.PORT = 8433
con = ldap.initialize('LDAP://vnhqpdc03.hcnet.vn:389')
def LoginLDAP (request):
    username = ''
    password =''
    state = ''
    
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #user1 = authenticate(username = request.GET.get('username'), password = request.GET.get('password') )
        # con.simple_bind_s(username, password)
        # user = con.search_s('CN=users,DC=hcnet,DC=vn', ldap.SCOPE_SUBTREE)
        # print(user)
        try:
            con.simple_bind_s(username, password)
            user = con.search_s('CN=users,DC=hcnet,DC=vn', ldap.SCOPE_SUBTREE)
            state = 'Welcome ' 
            print (user)
        except ldap.INVALID_CREDENTIALS:
            state = 'Fail'
            user = con.search_s('CN=users,DC=hcnet,DC=vn', ldap.SCOPE_SUBTREE)
            print (user)
        except ldap.INVALID_DN_SYNTAX:
            state = 'Fail'
            user = con.search_s('CN=users,DC=hcnet,DC=vn', ldap.SCOPE_SUBTREE)
            print (user)
        except ldap.INVALID_SYNTAX:
            state = 'Fail'
            user = con.search_s('CN=users,DC=hcnet,DC=vn', ldap.SCOPE_SUBTREE)
            print (user)    
        # if user != []:
        #     state = 'Welcome ' + str(user)
        # else:
        #     state = 'Not valid'
    return render(request, 'Login.html',{
        'state' : state + username, 'username' : username
    }
    )


