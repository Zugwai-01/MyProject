"""college_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from college_management import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup',views.homepage,name='homepage'),
    url(r'^students/',include('college_management.urls')),
    #url(r'^course/',include('college_management.urls')),
    url(r'^departments/',include('college_management.urlsDepartment')),
    url(r'^library/',include('college_management.urlsLibrary')),
    url(r'^about/',include('college_management.urlsAbout')),
    url(r'^news/',include('college_management.urlsNews')),
    url(r'^StudentCouncil/',include('college_management.urlsStudentcouncil')),
    #url(r'^staffs/',include('college_management.urls')),
    url(r'^$',views.index,name='index'),



]
