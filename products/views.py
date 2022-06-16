from django.db.models import fields
from django.shortcuts import render
from . models import Products
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class IndexPage(ListView):
    model = Products
    template_name = "index.html"



class IndexDetail(LoginRequiredMixin,DetailView,):
    model = Products
    template_name = 'indexdetail.html'


class Addpro(LoginRequiredMixin,CreateView,):
    model = Products
    template_name = 'addpro.html'
    fields = [
        'Product_name',
        'img',
        'price',
        'subtitle',
        'desc',

        'quenty'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpProduct(LoginRequiredMixin,UserPassesTestMixin,  UpdateView,):
    model = Products
    template_name = 'update.html'
    fields = [
        'Product_name',
        'img',
        'price',
        'subtitle',
        'desc',
        'quenty'
    ]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeletePro( LoginRequiredMixin,UserPassesTestMixin ,DeleteView,):

    model = Products
    template_name = 'deletepro.html'
    success_url = reverse_lazy('home')


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user