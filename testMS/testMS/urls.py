
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginLDAP, name = 'login'),
    path (r'VNpost/', include('VNpost.urls')),
]
