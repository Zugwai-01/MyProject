from django.conf.urls import url
from college_management import views

app_name ='news'

urlpatterns = [

    url(r'^News/$',views.news,name='news'),



]
