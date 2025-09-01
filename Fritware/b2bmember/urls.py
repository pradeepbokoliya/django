from django.urls import path
from b2bmember import views


urlpatterns = [
    path('memberlogin/', views.member_login, name='member_login'),
    path('dt/', views.dt, name='dt_login'), 
    path('rt/', views.rt, name='rt_login'), 
]
