from django.conf.urls import url
from college_management import views

app_name ='about'

urlpatterns = [

    url(r'^About/$',views.about,name='about'),



]
