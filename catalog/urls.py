from django.urls import path
from catalog.views import (HomeView, ProductUpdateView, ContactsView, ProductDetailView, ProductCreateView,ProductDeleteView,
                           CategoryProductView, CategoryProductDetailView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name



urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('category/', CategoryProductView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryProductDetailView.as_view(), name='category_products'),
]