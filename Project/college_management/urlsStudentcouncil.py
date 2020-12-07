from django.conf.urls import url
from college_management import views

app_name ='Studentcouncil'

urlpatterns = [

    url(r'^Studentcouncil/$',views.Studentcouncil,name='Studentcouncil'),



]
