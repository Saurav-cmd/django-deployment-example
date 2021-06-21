from django.conf.urls import url
from levelfive_second_app import views

app_name = 'levelfive_second_app'

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^register/$',views.register,name = 'register'),
    url(r'^login/$',views.userlogin,name = 'userlogin'),
]
