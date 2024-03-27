from django.urls import path
from .views.registration import signup_view

urlpatterns = [
    path('register/', signup_view, name = 'user_registration'),

]