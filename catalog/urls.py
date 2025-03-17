from django.urls import path
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductCreateView,ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name



urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_create/', ProductCreateView.as_view(), name='product_create')

]
#
# urlpatterns = [
#     path('', HomeView.as_view(), name='home'),
#     path('contacts/', ContactsView.as_view(), name='contacts'),
#     path('products/', ProductListView.as_view(), name='product_list'),
#     path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
#     path('products/create/', ProductCreateView.as_view(), name='product_create'),
#     path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
#     path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
# ]