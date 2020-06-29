from django.urls import path

from . import views

urlpatterns = [
    #path('', views.login, name='login'),
    path('login', views.UserView.loginwithpassword, name='login'),
    path('signup', views.UserView.signup, name='signup'),
]
