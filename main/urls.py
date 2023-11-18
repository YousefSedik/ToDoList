from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('Home/', views.home, name = 'home'),
    path('sign-up', views.sign_up, name = 'sign_up'),
    path('delete/<int:pk>', views.delete_todo, name='delete_todo'),
    path('check_uncheck<int:pk>', views.check_uncheck, name='check_uncheck')
]