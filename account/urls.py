from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import hello, AccountCreateView

app_name = 'account'

urlpatterns = [
    path('hello/', hello, name='hello'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
]