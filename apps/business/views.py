from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.messages.views import SuccessMessageMixin

from .models import VendasProdutos
from .forms import VendasProdutosForm, EditarVendasProdutosForm



# Create your views here.
class VendasView(TemplateView):
    template_name = "business/vendas.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['vendas'] = VendasProdutos.objects.filter(concluido=False)
        return context


class VendaCreateView(SuccessMessageMixin, CreateView):
    template_name = "business/cadastrar-venda.html"
    model = VendasProdutos
    form_class = VendasProdutosForm
    success_url = '/negocios/'
    success_message = "%(produto)s foi cadastrado com  successo!!!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.criador_por = self.request.user
        return super(VendaCreateView, self).form_valid(form)


class VendaDetailView(DetailView):
    template_name = "business/detalhe-venda.html"
    model = VendasProdutos

    def get(self, request, *args, **kwargs):
        venda = get_object_or_404(VendasProdutos, pk=kwargs['pk'])
        context = {'venda': venda}
        return render(request, 'business/detalhe-venda.html', context)



class VendaUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "business/cadastrar-venda.html"
    model = VendasProdutos
    form_class = EditarVendasProdutosForm
    success_url = '/negocios/'
    success_message = "%(produto)s foi alterado com  successo!!!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.ultima_alteracao_por = self.request.user
        return super(VendaUpdateView, self).form_valid(form)


class ConcluirVendaUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "business/concluir-venda.html"
    fields = ['concluido', 'concluido_por']
    model = VendasProdutos
    #success_url = reverse('venda_produtos')
    success_url = '/negocios/'
    success_message = "Venda finalizada com  successo!!!"


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.concluido_por = self.request.user
        obj.concluido = True
        return super(ConcluirVendaUpdateView, self).form_valid(form)


class HistoricoVendaListView(ListView):
    template_name = "business/historico-vendas.html"

    model = VendasProdutos
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historico_vendas'] = VendasProdutos.objects.filter(concluido=True)
        return context