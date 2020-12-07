from django.conf.urls import url
from college_management import views

app_name ='college_managements'

urlpatterns = [

    url(r'^departments/$',views.departments,name='departments'),



]
