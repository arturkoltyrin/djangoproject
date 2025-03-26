from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product
from catalog.forms import ProductForm, ProductModeratorForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils import timezone


class HomeView(ListView):
    model = Product
    template_name = 'catalog/base.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_moderated=True, is_available=True)

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
        return Product.objects.filter(is_moderated=True, is_available=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        fform.instance.owner = self.request.user
        form.instance.is_moderated = False
        form.instance.is_available = False
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.is_superuser

    def handle_no_permission(self):
        raise PermissionDenied

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

    def handle_no_permission(self):
        raise PermissionDenied

    def get_form_class(self):
        if self.request.user.is_superuser:
            return ProductForm
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        if self.request.user.has_perm("catalog.remove_any_product"):
            return ProductModeratorForm
        return ProductForm



