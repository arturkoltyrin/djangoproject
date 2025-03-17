from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product
from catalog.forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    model = Product
    template_name = 'catalog/base.html'
    context_object_name = 'products'

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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')