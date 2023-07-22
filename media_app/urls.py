from django.urls import path
from . import views

urlpatterns = [
    path('sign_up', views.SignUp.as_view(), name='media_app_sign_up'),
    path('', views.index, name='media_app_index')
]
