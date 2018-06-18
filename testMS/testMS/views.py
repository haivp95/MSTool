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
        searchFilter = "uid=tri.nh2"
      
        # print (con.result)
        con.simple_bind_s(username, password)
        print (searchFilter)
        user = con.search_s('CN=users,DC=hcnet,DC=vn', ldap.SCOPE_SUBTREE)
        
        # Cred = con.connection(username = request.GET.get('username'), password = request.GET.get('password') )
        # # print (Cred)
        #user = authenticate(username = 'admin', password =  'Tuongvi1')
        print(user)
        if user != []:
            #login(request, user)
            #state = [value[0] for value in result[0][1].values()]
            # Returns 2-element list, name and surname
            state = 'Welcome ' + str(user)
        else:
            state = 'Not valid'
    return render(request, 'login/Login.html',{
        'state' : state, 'username' : username
    }
    )


