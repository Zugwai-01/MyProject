from django.conf.urls import url
from college_management import views

#Template Tagging
app_name ='college_management'


urlpatterns = [
    url(r'^homepage/$',views.homepage,name='homepage'),
    url(r'^index/$',views.index,name='index'),



]
