from pydoc import visiblename
from django.urls import path
from . import views

urlpatterns = [
    path("blogsite/", views.home_page),
    path("signuppage/", views.signup_page),
#     path("signuppage/", views.signup_page),
]

