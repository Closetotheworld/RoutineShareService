from django.urls import path, include
from .views import hello, AccountCreateView

app_name = 'account'

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('create/', AccountCreateView.as_view(), name='create'),
]