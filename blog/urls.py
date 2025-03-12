from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('home/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('home/', BlogListView.as_view(), name='home'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
]