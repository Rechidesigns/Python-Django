from pydoc import visiblename
from django.urls import path
from . import views

urlpatterns = [
    path("rechi/", views.home_page),
    path("anotherpage/", views.another_page),
    path("signuppage/", views.signup_page),
]

