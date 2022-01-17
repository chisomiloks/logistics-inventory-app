from nntplib import ArticleInfo
from django.views.generic import (
    DetailView, 
    ListView,
)
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy

from .models import Inventory


# Create your views here.
class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory_list.html'


class InventoryDetailView(LoginRequiredMixin, DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'


class InventoryDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Inventory
    template_name = 'inventory_delete.html'
    success_url = reverse_lazy('inventory_list')

    def test_func(self):
        obj = self.get_object()
        return obj.merchant == self.request.user


class InventoryUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Inventory
    template_name = 'inventory_edit.html'
    fields = ('title', 'description', 'specifications', 'manufacturer', 'quantity')

    def test_func(self):
        obj = self.get_object()
        return obj.merchant == self.request.user


class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    template_name = 'inventory_new.html'
    fields = ('title', 'description', 'specifications', 'manufacturer', 'quantity')

    def form_valid(self, form):
        form.instance.merchant = self.request.user
        return super().form_valid(form)