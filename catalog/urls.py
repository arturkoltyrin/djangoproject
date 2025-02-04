from django.urls import path, include

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts"),
    path("catalog/", include('catalog.urls', namespace="catalog")),
    path("", include('media.urls', namespace="media"))
]