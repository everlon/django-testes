from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Produto


class IndexView(ListView):
    models = Produto
    template_name = 'crud/index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'crud/produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('crud')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'crud/produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('crud')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'crud/produto_del.html'
    success_url = reverse_lazy('crud')
