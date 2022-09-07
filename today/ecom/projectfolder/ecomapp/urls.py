from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryView().as_view(), name="category_list"),
    path('categories/<int:category_id>/', views.CategoryDetailView.as_view(), name="category_detail"),
    path('products/', views.ProductView().as_view(), name="product_list"),
    path('products/<int:product_id>/', views.ProductDetailView.as_view(), name="product_detail"),
]