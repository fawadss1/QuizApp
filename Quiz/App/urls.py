from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('login', views.stdLogin, name='Login'),
    path('logout', views.stdLogout, name='Logout'),
    path('quiz', views.quiz, name='Quiz'),

]
