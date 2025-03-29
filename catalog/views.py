from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product
from catalog.forms import ProductForm, ProductModeratorForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.urls import reverse


class HomeView(ListView):
    model = Product
    template_name = 'catalog/base.html'
    context_object_name = 'products'


    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated and self.request.user.is_moderator:
            return qs
        return qs.filter(is_available=True)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')

class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated and self.request.user.is_moderator:
            return qs
        return qs.filter(is_available=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        product = self.get_object()
        is_owner = self.request.user == product.owner
        has_delete_perms = self.request.user.has_perm('catalog:delete_product')
        return is_owner or has_delete_perms

    def handle_no_permission(self):
        raise PermissionDenied

    def get_form_class(self):
        product = self.get_object()
        if self.request.user.is_superuser:
            return ProductModeratorForm
        if self.request.user == product.owner:
            return ProductForm
        return ProductForm

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.id})

    def test_func(self):
        product = self.get_object()
        is_owner = self.request.user == product.owner
        has_unpublish_perms = self.request.user.has_perm('catalog.unpublish')
        return is_owner or has_unpublish_perms

    def get_form_class(self):
        product = self.get_object()
        if self.request.user.is_superuser:
            return ProductForm
        if self.request.user.is_moderator:
            return ProductModeratorForm
        return ProductForm



