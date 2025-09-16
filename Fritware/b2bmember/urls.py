from django.urls import path
from b2bmember import views


urlpatterns = [
    path('memberlogin/', views.member_login, name='member_login'),
    path('dt/', views.dt, name='dt_login'), 
    path('rt/', views.rt, name='rt_login'), 
    # path('test1/', views.user_login, name='test1'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]

