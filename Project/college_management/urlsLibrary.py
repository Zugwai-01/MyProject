from django.conf.urls import url
from college_management import views

app_name ='library'

urlpatterns = [

    url(r'^Library/$',views.library,name='library'),



]
