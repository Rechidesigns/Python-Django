from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path("", views.home_page, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>", views.post_detail, name="post_detail"),
    # path("<int:num1>/<int:num2>", views.thisisit)
]

