from django.urls import path
from b2badmin import views


urlpatterns = [
    path('createmember/', views.createMember, name='createmember'), 
]