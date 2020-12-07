from django.conf.urls import url
from college_management import views



urlpatterns = [
    url(r'^$',views.form_name,name='form_name'),



]
