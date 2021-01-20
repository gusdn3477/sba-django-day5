from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('git', views.git),
    path('test', views.test),
    path('signup', views.signup),
    path('login', views.login),
]
