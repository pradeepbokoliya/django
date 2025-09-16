
from django.urls import path
from b2b import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    
]