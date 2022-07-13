from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from .models import VendasProdutos, ComprasProdutos
from .forms import VendasProdutosForm, EditarVendasProdutosForm
from .forms import ComprasProdutosForm, EditarComprasProdutosForm
from datetime import datetime

import logging


logger = logging.basicConfig(filename="vendas.log")
logger = logging.getLogger('django')
now = datetime.now() # current date and time



# Views para Vendas de Produtos .

class VendasView(TemplateView):
    template_name = "business/vendas.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['vendas'] = VendasProdutos.objects.filter(concluido=False)

        arq = open("Ctos.log")
        linhas = arq.readlines()
        #logs = []
        #for linha in linhas:
            #logs.append(linha)
            #print(linha)
        context['linhas'] = linhas
    
        return context


class VendaCreateView(SuccessMessageMixin, CreateView):
    template_name = "business/cadastrar-venda.html"
    model = VendasProdutos
    form_class = VendasProdutosForm
    success_url = '/negocios/vendas/'
    success_message = "%(produto)s foi cadastrado com  successo!!!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.criador_por = self.request.user
    
        logger.info(
            f'{now.strftime(" %m/%d/%Y, %H:%M:%S")} | user: {str(self.request.user)} | cadastrou uma venda de {str(obj.quantidade)}: {str(obj.produto)}')

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
    success_url = '/negocios/vendas/'
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
    success_url = '/negocios/vendas/'
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

# -----------------------------------------------------------------------------------------------
# Views para Vendas de Produtos.

class ComprasView(TemplateView):
    template_name = "business/compras.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['compras'] = ComprasProdutos.objects.filter(concluido=False)
        return context


class CompraCreateView(SuccessMessageMixin, CreateView):
    template_name = "business/cadastrar-compra.html"
    model = ComprasProdutos
    form_class = ComprasProdutosForm
    success_url = '/negocios/compras/'
    success_message = "%(produto)s foi cadastrado com  successo!!!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.criado_por = self.request.user
        return super(CompraCreateView, self).form_valid(form)


class CompraUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "business/cadastrar-compra.html"
    model = ComprasProdutos
    form_class = EditarComprasProdutosForm
    success_url = '/negocios/compras/'
    success_message = "%(produto)s foi alterado com  successo!!!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.ultima_alteracao_por = self.request.user
        return super(CompraUpdateView, self).form_valid(form)


class CompraDetailView(DetailView):
    template_name = "business/detalhe-compra.html"
    model = ComprasProdutos

    def get(self, request, *args, **kwargs):
        compra = get_object_or_404(ComprasProdutos, pk=kwargs['pk'])
        context = {'compra': compra}
        return render(request, 'business/detalhe-compra.html', context)


class ConcluirCompraUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "business/concluir-compra.html"
    fields = ['concluido', 'concluido_por']
    model = ComprasProdutos
    success_url = '/negocios/compras/'
    success_message = "Compra finalizada com successo!!!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.concluido_por = self.request.user
        obj.concluido = True
        return super(ConcluirCompraUpdateView, self).form_valid(form)


class HistoricoCompraListView(ListView):
    template_name = "business/historico-compras.html"
    model = ComprasProdutos
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historico_compras'] = ComprasProdutos.objects.filter(concluido=True)
        return context